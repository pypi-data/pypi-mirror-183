'''
@File    :   data_analysis.py
@Time    :   2022/10/25 23:20:16
@Author  :   Pengyao Ping
@Version :   1.0
@Contact :   Ping.Pengyao@gmail.com
@desc    : 
'''

from collections import Counter
import collections
import math
from Bio import SeqIO
import os
import editdistance
import xlsxwriter
from SRRec.utils import *

class DataAnalysis():
    """
    A class to evaluate an error correction method.
    """
    def __init__(self, logger, config):
        """
        initialize the DataAnalysis class

        Args:
            logger (class): customized logging
            config (class): parameters setting using configparser
        """
        self.logger = logger
        self.config = config
        self.logger.info(f'Raw dataset: {config.input_file}')
        self.logger.info(f'Correct dataset: {config.correct_data}')
        self.logger.info(f'Ground truth dataset: {config.ground_truth_data}')
        if os.path.exists(self.config.result_dir):
            self.logger.info("Directory '% s' already exists" % self.config.result_dir)
            # for f in os.listdir(self.config.result_dir):
            #     os.remove(os.path.join(self.config.result_dir, f))
        else:
            os.makedirs(self.config.result_dir)
            self.logger.info("Directory '% s' created" % self.config.result_dir)
        bases = config.correct_data.split('/')[-1]
        prefix = bases.split('.' + parse_file_type(config.correct_data))[0]
        self.result_file = os.path.join(config.result_dir, prefix + '.xlsx')
        self.workbook_flie = xlsxwriter.Workbook(self.result_file)
        
    def percentage(self, part, whole):
        """
        percentage calculation

        Args:
            part (int): _description_
            whole (int): _description_

        Returns:
            str: percentage, if whole equals 0, return 'Not exist in raw'
        """
        if whole != 0:
            Percentage = 100 * float(part)/float(whole)
            return str(Percentage) + "%"
        else:
            return str('Not exist in raw')
        
    def ranking(self, num, num_lst):
        """
        get read count's ranking

        Args:
            num (int): read count
            num_lst (list): a list of read counts

        Returns:
            int: ranking
        """
        for n in num_lst:
            if num == n:
                return num_lst.index(n) + 1

    def evaluation(self):
        """
        Invoke the function to run the whole evaluation process, and write the result to files. 
        """
        # read the input using SeqIO
        raw_record_iterator, raw_file_tye = parse_data(self.config.input_file)
        correct_record_iterator, correct_file_tye = parse_data(self.config.correct_data)
        raw_seqs = []
        correct_seqs = []

        self.raw_len2seqs_dict = {}
        self.raw_len_lst = []
        total_reads_num = 0
        for raw_item, correct_item in zip(raw_record_iterator, correct_record_iterator):
            raw_seq = str(raw_item.seq)
            raw_seqs.append(raw_seq)
            correct_seqs.append(str(correct_item.seq))
            
            ll = len(raw_seq)
            self.raw_len_lst.append(ll)
            self.raw_len2seqs_dict.setdefault(ll, []).append(raw_seq)
            total_reads_num += 1

        raw_read2count = Counter(raw_seqs)
        correct_read2count = Counter(correct_seqs)

        raw_read2count_val_lst = list(raw_read2count.values())
        raw_read2count_val_lst.sort(reverse=True)

        correct_read2count_val_lst = list(correct_read2count.values())
        correct_read2count_val_lst.sort(reverse=True)

        raw_counts_lst = raw_read2count_val_lst[ : self.config.top_n * 10]
        correct_counts_lst = correct_read2count_val_lst[ : self.config.top_n * 10]
        
        # self.workbook_flie = xlsxwriter.Workbook(self.result_file)
        worksheet = self.workbook_flie.add_worksheet('AbundanceChange')
        # Use the worksheet object to write
        # data via the write() method.
        worksheet.write('A1', 'Read')
        worksheet.write('B1', 'Count after Correction')
        worksheet.write('C1', 'Count before Correction')
        worksheet.write('D1', 'Abundance change percentage')
        worksheet.write('E1', 'Rank after Correction')
        worksheet.write('F1', 'Rank before Correction')

        row = 1
        col = 0
        for read, count in correct_read2count.most_common(self.config.top_n):
            worksheet.write(row, col, read)
            worksheet.write(row, col + 1, count)
            
            raw_read_count = raw_read2count[read]
            worksheet.write(row, col + 2, raw_read_count)
            abundance_percentage = self.percentage(count - raw_read_count, raw_read_count)
            worksheet.write(row, col + 3, abundance_percentage)

            correct_rank = self.ranking(count, correct_counts_lst)
            worksheet.write(row, col + 4, correct_rank)
            raw_rank = self.ranking(raw_read_count, raw_read2count_val_lst)
            worksheet.write(row, col + 5, raw_rank)
            row += 1

        self.logger.debug(f'Ground truth: {self.config.ground_truth_data}')
        if self.config.ground_truth_data:
            self.evaluation_with_groundtruth()
        # no ground truth entropy
        self.evaluation_without_groundtruth(raw_read2count, correct_read2count, total_reads_num)
        return

    # rely on read frequency instead of sequecing id
    def evaluation_with_groundtruth(self):
        """
        Evaluating an error correction method using raw, true and corrected data based on read frequency instead of sequecing id
        """
        read_level = {'tp':0, 'fp':0, 'tn':0, 'fn':0}
        base_level = {'tp':0, 'fp':0, 'tn':0, 'fn':0}
        
        true_records, true_f_tye = parse_data_index(self.config.ground_truth_data)
        error_records, err_f_tye = parse_data_index(self.config.input_file)
        correct_records, cor_f_tye = parse_data_index(self.config.correct_data)

        total_reads_num = 0
        # for calculating entropy
        correct_errfree_seqs = []
        correct_err_seqs = []
        raw_errfreee_seqs = []
        raw_err_seqs = []

        true_seqs_lst = []
        raw_seqs_lst = []
        correct_seqs_lst = []
        true_umi2seqs = {}
        raw_umi2seqs = {}
        correct_umi2seqs = {}

        true_seq2umi = {}
        for name in error_records:
            true_seq = str(true_records[name].seq)
            raw_seq = str(error_records[name].seq)
            correct_seq = str(correct_records[name].seq) 

            umi_base = str(true_records[name].description).split('//')[0]
            umi = umi_base.split(':')[1]
            true_umi2seqs.setdefault(umi, []).append(true_seq)
            raw_umi2seqs.setdefault(umi, []).append(raw_seq)
            correct_umi2seqs.setdefault(umi, []).append(correct_seq)

            true_seq2umi.setdefault(true_seq, []).append(umi)

            true_seqs_lst.append(true_seq)     
            raw_seqs_lst.append(raw_seq)
            correct_seqs_lst.append(correct_seq)

        raw_read2count = collections.Counter(raw_seqs_lst)
        true_read2count = collections.Counter(true_seqs_lst)
        correct_read2count = collections.Counter(correct_seqs_lst)

        num = 0
        read_num = 0
        for seq in true_seq2umi:
            unique_umi = set(true_seq2umi[seq])
            if len(unique_umi) > 1:
                num += 1
                read_num += correct_read2count[seq]
                # print(unique_umi, )
        print(num, read_num)
############################################################################################
        # merge same sequences with different umis
        true_umis2seqs = {}
        raw_umis2seqs = {}
        correct_umis2seqs = {}
        for seq in true_seq2umi:
            unique_umi = list(set(true_seq2umi[seq]))
            umi_num = len(unique_umi)
            umi = tuple(unique_umi)
            if umi_num == 1:
                tmp_umi = unique_umi[0]
                true_umis2seqs[umi] = true_umi2seqs[tmp_umi]
                raw_umis2seqs[umi] = raw_umi2seqs[tmp_umi]
                correct_umis2seqs[umi] = correct_umi2seqs[tmp_umi]   
            else:
                for tmp_umi in unique_umi:
                    true_umis2seqs.setdefault(umi, []).extend(true_umi2seqs[tmp_umi])   
                    raw_umis2seqs.setdefault(umi, []).extend(raw_umi2seqs[tmp_umi])
                    correct_umis2seqs.setdefault(umi, []).extend(correct_umi2seqs[tmp_umi])      


############################################################################################
        fn_lst = []
        positive_fp_lst = []
        # ii = 0
        original_high_ambiguous = []
        # for umi in true_umi2seqs:
        #     true_seqs = true_umi2seqs[umi]
        #     raw_seqs = raw_umi2seqs[umi]
        #     correct_seqs = correct_umi2seqs[umi]

        for umi in true_umis2seqs:
            true_seqs = true_umis2seqs[umi]
            raw_seqs = raw_umis2seqs[umi]
            correct_seqs = correct_umis2seqs[umi]

            true_seqs_len = len(true_seqs)
            total_reads_num += true_seqs_len
            # raw base level
            total_positive_bases = 0
            total_negative_bases = 0
            # raw read level
            total_positive_reads = 0
            total_negative_reads = 0

            # correction base level
            cor_positive_bases = 0
            cor_negative_bases = 0
            # correction read level
            cor_positive_reads = 0
            cor_negative_reads = 0
            
            if len(set(true_seqs)) != 1:
                self.logger.exception("UMI(s) contain(s) more than one true sequences.")
            t_seq = true_seqs[0]
            r_seqs = list(set(raw_seqs))
            r_seq2counts = collections.Counter(raw_seqs)
            if len(r_seqs) > 1:
                for r_seq in r_seqs:
                    t_r_dis = editdistance.eval(t_seq, r_seq)
                    # if t_r_dis == 1 or t_r_dis == 2:
                    if t_r_dis == 1:
                        r_seq_count = raw_read2count[r_seq]
                        t_seq_count = raw_read2count[t_seq]
                        if r_seq_count > 5 and t_seq_count > 5:
                            # original_high_ambiguous.append([umi, t_r_dis, t_seq, t_seq_count, r_seq, r_seq_count, r_seq2counts[r_seq]])
                            line = [str(umi), t_r_dis, t_seq, t_seq_count, r_seq, r_seq_count, r_seq2counts[r_seq]]
                            if line not in original_high_ambiguous:
                                original_high_ambiguous.append(line)
                # ii += 1

            for i in range(true_seqs_len):
                raw_seq = raw_seqs[i]
                true_seq = true_seqs[i]
                seq_len = len(true_seq)
                true_raw_dis = editdistance.eval(true_seq, raw_seq)
                # raw base level
                total_positive_bases += true_raw_dis
                total_negative_bases += seq_len - true_raw_dis
                # raw read level
                if true_raw_dis == 0:
                    raw_errfreee_seqs.append(raw_seq)
                    total_negative_reads += 1
                else:
                    raw_err_seqs.append(raw_seq)
                    total_positive_reads += 1
                # after correction
                correct_seq = correct_seqs[i]
                true_cor_dis = editdistance.eval(true_seq, correct_seq)
                # correction base level
                cor_positive_bases += true_cor_dis
                cor_negative_bases += seq_len - true_cor_dis
                # correction read level
                if true_cor_dis == 0:
                    correct_errfree_seqs.append(correct_seq)
                    cor_negative_reads += 1
                else: 
                    correct_err_seqs.append(correct_seq)
                    cor_positive_reads += 1
            # note: for any postive read, if it is modified correctly, tp will increase one. if it is modified incorrectly, it will keep as a fn rather than a fp. Similarly, for any negative read, 
            # base level
            if total_positive_bases >= cor_positive_bases:
                base_level['tp'] += total_positive_bases - cor_positive_bases
                base_level['fn'] += cor_positive_bases  
            if total_negative_bases >= cor_negative_bases:  
                base_level['tn'] += cor_negative_bases
                base_level['fp'] += total_negative_bases - cor_negative_bases

            if total_positive_bases < cor_positive_bases:
                base_level['tp'] += 0
                base_level['fn'] += total_positive_bases
                # self.logger.warning(f'Base-level Evaluation: introduced additional {cor_positive_bases - total_positive_bases} positive bases after correction for UMI {str(umi)}')  
            if total_negative_bases < cor_negative_bases:
                base_level['tn'] += total_negative_bases
                base_level['fp'] += 0    
                # self.logger.warning(f'Base-level Evaluation: introduced additional {cor_negative_bases - total_negative_bases} negative bases after correction for UMI {str(umi)}')   

            # read level
            if total_positive_reads >= cor_positive_reads:
                read_level['tp'] += total_positive_reads - cor_positive_reads
                read_level['fn'] += cor_positive_reads  
            if total_negative_reads >= cor_negative_reads:
                read_level['tn'] += cor_negative_reads
                read_level['fp'] += total_negative_reads - cor_negative_reads  
            if total_positive_reads < cor_positive_reads:
                read_level['tp'] += 0
                read_level['fn'] += total_positive_reads
                self.logger.warning(f'Read-level Evaluation: introduced additional {cor_positive_reads - total_positive_reads} positive reads after correction for UMI {str(umi)}') 
            if total_negative_reads < cor_negative_reads:
                read_level['tn'] += total_negative_reads
                read_level['fp'] += 0
                # self.logger.warning(f'Read-level Evaluation: introduced additional {cor_negative_reads - total_negative_reads} negative reads after correction for UMI {str(umi)}') 

            ## fn
            raw_positive_seqs = set(raw_seqs) - set(true_seqs)
            untouched_positive_seqs = set(correct_seqs) - set(true_seqs)

            if len(raw_positive_seqs) > 0:
                if len(untouched_positive_seqs) > 0:
                    # true_group = [t_seq, true_read2count[t_seq], raw_read2count[t_seq], correct_read2count[t_seq]]
                    for seq in untouched_positive_seqs:
                        fn_lst.append([str(umi), t_seq, raw_read2count[t_seq], seq, raw_read2count[seq], correct_read2count[t_seq], correct_read2count[seq]])                                        
            # fp
            # elif len(raw_positive_seqs) == 0:
            #     if len(untouched_positive_seqs) > 0:
            #         true_group = [t_seq, true_read2count[t_seq], raw_read2count[t_seq], correct_read2count[t_seq]]
            #         correct_group = []
            #         for item in untouched_positive_seqs:
            #             correct_group.append([item, true_read2count[item], raw_read2count[item], correct_read2count[item]])  
            #         positive_fp_lst.append([umi, str(true_group), str(correct_group)]) 

            # if len(raw_positive_seqs) > 0:
            #     if len(untouched_positive_seqs) > 0:
            #         intersec_seqs = untouched_positive_seqs & raw_positive_seqs
            #         raw_group = []
            #         if len(intersec_seqs) > 0:
            #             for item in intersec_seqs:
            #                 raw_group.append([item, true_read2count[item], raw_read2count[item], correct_read2count[item]])                    
            #         correct_group = []
            #         true_group = [t_seq, true_read2count[t_seq], raw_read2count[t_seq], correct_read2count[t_seq]]
            #         for item in untouched_positive_seqs:
            #             correct_group.append([item, true_read2count[item], raw_read2count[item], correct_read2count[item]])  
            #         fn_lst.append([umi, str(true_group), str(raw_group), str(correct_group)])   

            #         generate_fp_seqs = untouched_positive_seqs - raw_positive_seqs   
            #         correct_group2 = []
            #         if len(generate_fp_seqs) > 0:
            #             for seq in generate_fp_seqs:
            #                 correct_group2.append([seq, true_read2count[seq], raw_read2count[seq], correct_read2count[seq]])  
            #             positive_fp_lst.append([umi, str(true_group), str(correct_group2)])                                       
            # # fp
            # elif len(raw_positive_seqs) == 0:
            #     if len(untouched_positive_seqs) > 0:
            #         true_group = [t_seq, true_read2count[t_seq], raw_read2count[t_seq], correct_read2count[t_seq]]
            #         correct_group = []
            #         for item in untouched_positive_seqs:
            #             correct_group.append([item, true_read2count[item], raw_read2count[item], correct_read2count[item]])  
            #         positive_fp_lst.append([umi, str(true_group), str(correct_group)])                    


            # if len(untouched_positive_seqs) > 0:
            #     intersec_seqs = untouched_positive_seqs & raw_positive_seqs
            #     true_group = [true_seq, true_read2count[true_seq], raw_read2count[true_seq], correct_read2count[true_seq]]
            #     raw_group = []
            #     if len(intersec_seqs) > 0:
            #         for item in intersec_seqs:
            #             raw_group.append([item, true_read2count[item], raw_read2count[item], correct_read2count[item]])
            #     correct_group = []
            #     for item in untouched_positive_seqs:
            #         correct_group.append([item, true_read2count[item], raw_read2count[item], correct_read2count[item]])
            #     fn_lst.append([umi, str(true_group), str(raw_group), str(correct_group)])
        #########
        # high_ambi_worksheet = self.workbook_flie.add_worksheet('high_ambiguous')
        # for r_n, data in enumerate(original_high_ambiguous):
        #     high_ambi_worksheet.write_row(r_n, 0, data)

        # fn_worksheet = self.workbook_flie.add_worksheet('fn')
        # for row_num, data in enumerate(fn_lst):
        #     fn_worksheet.write_row(row_num, 0, data)

        # fp_worksheet = self.workbook_flie.add_worksheet('positive_fp')
        # for row_num, data in enumerate(positive_fp_lst):
        #     fp_worksheet.write_row(row_num, 0, data)

        self.evaluation_metircs(base_level, 'Base level')
        self.evaluation_metircs(read_level, 'Read level') 
        rawset_entropy = self.set_entropy(len(raw_err_seqs), len(raw_errfreee_seqs), total_reads_num)
        correctset_entropy = self.set_entropy(len(correct_err_seqs), len(correct_errfree_seqs), total_reads_num)
        self.save_entropy('Dataset Entropy', rawset_entropy, correctset_entropy)
        return

    def evaluation_without_groundtruth(self, raw_read2count, correct_read2count, total_reads_num):
        """
        Evaluating an error correction method using raw and corrected data (before and after) base on defined read counts entropy

        Args:
            raw_read2count (dict): A dictionary to save reads (keys) and its counts (values) for raw dataset
            correct_read2count (dict): A dictionary to save reads (keys) and its counts (values) for corrected dataset of raw dataset
            total_reads_num (int): the number of the total reads
        """
        rawset_entropy_noTruth = self.read_counts_entropy(raw_read2count, total_reads_num)
        correctset_entropy_noTruth = self.read_counts_entropy(correct_read2count, total_reads_num)
        self.save_entropy('ReadCountEntropy', rawset_entropy_noTruth, correctset_entropy_noTruth) 
        self.workbook_flie.close()
        return
        
    def evaluation_metircs(self, confusion_dict, sheet_name):
        """
        Evaluation metrics

        Args:
            confusion_dict (dict): A dictionary consists the values of TP, TN, FP and FN
            sheet_name (str): A string to indicate a sheet name of a csv file
        """
        tp = confusion_dict['tp']
        tn = confusion_dict['tn']
        fp = confusion_dict['fp']
        fn = confusion_dict['fn']
        if tp + tn + fp + fn != 0: 
            accuracy = (tp + tn) / (tp + tn + fp + fn)
        else:
            accuracy = "None"
        if tp + fp != 0:
            precision = tp / (tp + fp)
        else:
            precision = "None"
        if tp + fn != 0:
            recall = tp / (tp + fn)
            gain = (tp - fp) / (tp + fn)
        else:
            recall = "None"
            gain = "None"
        if fp + tn != 0:
            fall_out = fp / (fp + tn)
        else:
            fall_out = "None"
        # self.logger.info(sheet_name)
        self.logger.info("{}: accuracy: {}, precision: {}, recall: {}, gain: {}, fall-out: {}".format(sheet_name, accuracy, precision, recall, gain, fall_out))
        worksheet3 = self.workbook_flie.add_worksheet(sheet_name)
        worksheet3.write('A1', 'TP')
        worksheet3.write('A2', tp)
        worksheet3.write('B1', 'FP')
        worksheet3.write('B2', fp)
        worksheet3.write('C1', 'FN')
        worksheet3.write('C2', fn)
        worksheet3.write('D1', 'TN')
        worksheet3.write('D2', tn)

        worksheet3.write('E1', 'Accuracy')
        worksheet3.write('E2', accuracy)
        worksheet3.write('F1', 'Precision')
        worksheet3.write('F2', precision)
        worksheet3.write('G1', 'Recall')
        worksheet3.write('G2', recall)
        worksheet3.write('H1', 'Gain')
        worksheet3.write('H2', gain)
        worksheet3.write('I1', 'Fall-out')
        worksheet3.write('I2', fall_out)
        return

    def entropy(self, seqs_num, total_num):
        """
        part of the dataset entropy to measure the reads impurity of error-contained and error-free
        Args:
            seqs_num (int): the number of error-contained or error-free reads
            total_num (int): the number of total reads

        Returns:
            float: part of the dataset entropy
        """
        p = seqs_num / total_num
        entropy_val = -(p * math.log2(p))
        return entropy_val

    def read_counts_entropy(self, read_count, total_num):
        """
        read count entropy calculation

        Args:
            read_count (dict): A dictionary to save reads (keys) and its counts (values) for dataset
            total_num (int): the number of total reads

        Returns:
            float: read count entropy 
        """
        entropy_val = 0
        for count in read_count.values():
            p = count / total_num
            entropy_val += -(p * math.log2(p))
            #+ (1-p) * math.log(1-p)
        return entropy_val

    def set_entropy(self, err_seqs_num, errfree_seqs_num, total_num):
        """
        dataset entropy to measure the reads impurity of error-contained and error-free

        Args:
            err_seqs_num (int): the number of error-conatined reads
            errfree_seqs_num (int): the number of error-free reads
            total_num (int): the number of total reads

        Returns:
            float: dataset entropy
        """
        # total_seqs = err_seqs + errfree_seqs
        # unique_len = len(set(total_seqs))
        err_entropy = self.entropy(err_seqs_num, total_num)
        errfree_entropy = self.entropy(errfree_seqs_num, total_num)
        return errfree_entropy + err_entropy

    def save_entropy(self, sheet_name, raw_set_entropy, correct_entropy):
        """
        save entropy result to a csv sheet

        Args:
            sheet_name (str): A string to indicate a sheet name of a csv file
            raw_set_entropy (float): raw dataset entropy
            correct_entropy (float): corrected dataset entropy
        """
        self.logger.info("{}: raw dataset entropy: {}, correct dataset entropy: {}".format(sheet_name, raw_set_entropy, correct_entropy))
        worksheet3 = self.workbook_flie.add_worksheet(sheet_name)
        worksheet3.write('A1', 'raw dataset entropy')
        worksheet3.write('B1', raw_set_entropy)
        worksheet3.write('A2', 'correct dataset entropy')
        worksheet3.write('B2', correct_entropy) 
        return   

    '''
    def evaluation_with_groundtruth0(self):
        read_level = {'tp':0, 'fp':0, 'tn':0, 'fn':0}
        base_level = {'tp':0, 'fp':0, 'tn':0, 'fn':0}
        true_records = SeqIO.index(self.config.ground_truth_data, parse_file_type(self.config.ground_truth_data))
        error_records = SeqIO.index(self.config.input_file, parse_file_type(self.config.input_file))
        correct_records = SeqIO.index(self.config.correct_data, parse_file_type(self.config.input_file))
        total_reads_num = 0
        # for calculating entropy
        correct_errfree_seqs = []
        correct_err_seqs = []
        raw_errfreee_seqs = []
        raw_err_seqs = []

        true_seqs_lst = []
        raw_seqs_lst = []
        correct_seqs_lst = []
        for name in error_records:
            true_seq = str(true_records[name].seq)
            raw_seq = str(error_records[name].seq)
            correct_seq = str(correct_records[name].seq)   
            true_seqs_lst.append(true_seq)     
            raw_seqs_lst.append(raw_seq)
            correct_seqs_lst.append(correct_seq)
        raw_read2count = collections.Counter(raw_seqs_lst)
        true_read2count = collections.Counter(true_seqs_lst)
        correct_read2count = collections.Counter(correct_seqs_lst)

        fn_lst = []

        for name in error_records:
            total_reads_num += 1
            true_seq = str(true_records[name].seq)
            raw_seq = str(error_records[name].seq)
            correct_seq = str(correct_records[name].seq)

            true_raw_dis = editdistance.eval(true_seq, raw_seq)
            true_cor_dis = editdistance.eval(true_seq, correct_seq)
            raw_cor_dis = editdistance.eval(raw_seq, correct_seq)
            #
            if true_cor_dis == 0:
                correct_errfree_seqs.append(correct_seq)
            else:
                correct_err_seqs.append(correct_seq)

            # actual condition with no errors
            # negative conditions
            if true_raw_dis == 0:
                raw_errfreee_seqs.append(raw_seq)
                if true_cor_dis == 0:
                    base_level['tn'] += len(true_seq)
                    read_level['tn'] += 1
                else:
                    base_level['tn'] += len(true_seq) - true_cor_dis
                    base_level['fp'] += true_cor_dis
                    read_level['fp'] += 1
            # true_raw_dis != 0 which means actual condition contain errors 
            else:
                raw_err_seqs.append(raw_seq)
                if true_cor_dis == 0:
                    base_level['tp'] += true_raw_dis
                    base_level['tn'] += len(true_seq) - true_raw_dis
                    read_level['tp'] += 1
                else:
                    read_level['fn'] += 1
                    fn_lst.append([raw_seq, raw_read2count[raw_seq], true_seq, true_read2count[true_seq], correct_seq, correct_read2count[correct_seq]])
                    if raw_cor_dis == 0:
                        base_level['tn'] += len(true_seq) - true_raw_dis
                        base_level['fn'] += true_raw_dis # true_raw_dis == true_cor_dis
                    else:
                        # measure the distance change with ture sequence before and after correction
                        gap = true_raw_dis - true_cor_dis
                        if gap > 0: # distance decrease after correction
                            base_level['tp'] += gap
                            base_level['tn'] += len(true_seq) - true_raw_dis
                            base_level['fn'] += true_cor_dis
                        elif gap < 0:
                            base_level['tn'] += len(true_seq) - true_cor_dis
                            base_level['fp'] += abs(gap)
                            base_level['fn'] += true_raw_dis
                        else:
                            base_level['tn'] += len(true_seq) - true_cor_dis
                            base_level['fn'] += true_cor_dis
        worksheet = self.workbook_flie.add_worksheet('fn')
        for row_num, data in enumerate(fn_lst):
            worksheet.write_row(row_num, 0, data)
        self.evaluation_metircs(base_level, 'Base level')
        self.evaluation_metircs(read_level, 'Read level') 
        rawset_entropy = self.set_entropy(raw_err_seqs, raw_errfreee_seqs, total_reads_num)
        correctset_entropy = self.set_entropy(correct_err_seqs, correct_errfree_seqs, total_reads_num)
        self.save_entropy('Dataset Entropy', rawset_entropy, correctset_entropy)
        # self.workbook_flie.close()

        return
    '''        
    # def entropy0(self, seqs, total_num):
    #     read_count = Counter(seqs)
    #     entropy_val = 0
    #     for read, count in read_count.items():
    #         p = count / total_num
    #         entropy_val += -(p * math.log2(p))
    #     return entropy_val
