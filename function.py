import pandas as pd
import numpy as np


def clean_data(file):
    l1 = ['1.CO22U', '3.GLU1U', '4.BUN1U', '5.CRE1U', '6.CAZ1U', '7.ALB1U',
          '8.ALP1U', '9.ALT1U', '10.AST1U', '12.TBC1U', '13.TP-1U',
          '16.AMY1U', '25.CHO1U', '27.CKN1U', '34.DBC1U', '39.HDL1U',
          '44.PHO1U', '45.FE-1U', '46.LAC1U', '47.LDH1U', '48.LDL1U',
          '49.LIP1U', '50.LTM1G', '51.MG-1U', '54.TRF1G', '55.TRG1U',
          '57.UA-1U', '62.ACT1G', '63.CAR1G', '64.DIG1G', '65.GEN1G',
          '66.PHB1G', '67.PHY1G', '68.SAL1G', '69.THE1G', '70.TOB1G',
          '71.VPA1G', '97.Na', '98.K', '99.Cl']
    l2 = ["Co2", "Glucose", "BUN", "CRE", 'Calcium', 'Albumin', 'ALP', 'ALT', 'AST', 'TBC', 'TP',
          'Amylase', 'Cholestrol', 'CK', 'DBC', "HDL1U",
          'Phosphores', 'Iron', 'Lactic', 'LDH', 'LDL',
          "Lipase", "LTM", "Mg", "Transferin", "TRG", "Uric acid", "Acetaminophyn", "Carbamazepine", "Digoxin",
          "Gentamysin", "Phenobarbital", "Phenytoin",
          "Salicylates", "Theophylline", "Tobramycin", "VPA", 'Na', 'K', 'Cl']
    l3 = ['114.B/C', '115.GAP', '116.A/G', '118.IBIL', '120.OSMO', 'Lipemia', 'Icterus', 'Hemolysis']
    l4_1 = ['88891', '88901']
    l4_2 = ['88892', '88902']
    l4_3 = ['88893', '88903']
    l5 = ["qc1", "qc2", "qc3"]

    df = pd.read_csv(file)
    df.drop([df.index[0], df.index[1], df.index[2], df.index[3]], inplace=True)
    df.columns = df.iloc[0]
    df.drop([df.index[0]], inplace=True)
    df_new = df[["S. ID", "Test Name", "Conc."]]
    df_new.rename(columns={"S. ID": "ID", "Test Name": "Test", "Conc.": "Conc"}, inplace=True)
    df_new["Test"] = df_new["Test"].replace(l1, l2)
    df_new["ID"] = df_new["ID"].replace(l4_1, l5[0])
    df_new["ID"] = df_new["ID"].replace(l4_2, l5[1])
    df_new["ID"] = df_new["ID"].replace(l4_3, l5[2])

    df_new = df_new[df_new.Test.isin(l3) == False]
    df_new = df_new.astype({"Conc": float})
    return df_new



def mean_calculation(file,location):
    df = clean_data(file)
    df_mean = df.groupby(['ID', 'Test'])['Conc'].agg([np.mean, np.std])
    df_final = pd.DataFrame(df_mean)
    return df_final.to_csv(location)

