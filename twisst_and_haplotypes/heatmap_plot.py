import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

piv_data = pd.DataFrame()
gene_name = "AL1G35730"
path = "/netscratch/dep_mercier/grp_novikova/A.Lyrata/anna_g/" + gene_name + "_Eur_dipl_fin.csv"
heat_data2  = pd.read_csv(path, sep=",", header=None)
heat_data2 = heat_data2.rename(columns={0: "position", 1: "A", 2: "C", 3: "G", 4: "T", 5: "A_out", 6: "C_out", 7: "G_out", 8: "T_out"})
heat_data_pol = heat_data2[(heat_data2.A_out == (heat_data2.A_out + heat_data2.C_out + heat_data2.T_out + heat_data2.G_out))]
heat_data_pol = pd.concat([heat_data_pol, heat_data2[(heat_data2.C_out == (heat_data2.A_out + heat_data2.C_out + heat_data2.T_out + heat_data2.G_out))]])
heat_data_pol = pd.concat([heat_data_pol, heat_data2[(heat_data2.G_out == (heat_data2.A_out + heat_data2.C_out + heat_data2.T_out + heat_data2.G_out))]])
heat_data_pol = pd.concat([heat_data_pol, heat_data2[(heat_data2.T_out == (heat_data2.A_out + heat_data2.C_out + heat_data2.T_out + heat_data2.G_out))]])
heat_data_pol.A_out[heat_data_pol.A_out > 0] = 1
heat_data_pol.C_out[heat_data_pol.C_out > 0] = 1
heat_data_pol.G_out[heat_data_pol.G_out > 0] = 1
heat_data_pol.T_out[heat_data_pol.T_out > 0] = 1

heat_data_pol["ancestral"] = ((heat_data_pol.A * heat_data_pol.A_out)  + (heat_data_pol.C * heat_data_pol.C_out) + (heat_data_pol["T"] * heat_data_pol.T_out) + (heat_data_pol.G * heat_data_pol.G_out))
heat_data_pol["derived"] =  (heat_data_pol.A + heat_data_pol.C + heat_data_pol.G + heat_data_pol["T"]) - heat_data_pol.ancestral
piv_data["CE_2n"] = heat_data_pol.derived / (heat_data_pol.ancestral + heat_data_pol.derived) 

path = "/netscratch/dep_mercier/grp_novikova/A.Lyrata/anna_g/" + gene_name + "_Eur_tetr_fin.csv"
heat_data2  = pd.read_csv(path, sep=",", header=None)
heat_data2 = heat_data2.rename(columns={0: "position", 1: "A", 2: "C", 3: "G", 4: "T", 5: "A_out", 6: "C_out", 7: "G_out", 8: "T_out"})
heat_data_pol = heat_data2[(heat_data2.A_out == (heat_data2.A_out + heat_data2.C_out + heat_data2.T_out + heat_data2.G_out))]
heat_data_pol = pd.concat([heat_data_pol, heat_data2[(heat_data2.C_out == (heat_data2.A_out + heat_data2.C_out + heat_data2.T_out + heat_data2.G_out))]])
heat_data_pol = pd.concat([heat_data_pol, heat_data2[(heat_data2.G_out == (heat_data2.A_out + heat_data2.C_out + heat_data2.T_out + heat_data2.G_out))]])
heat_data_pol = pd.concat([heat_data_pol, heat_data2[(heat_data2.T_out == (heat_data2.A_out + heat_data2.C_out + heat_data2.T_out + heat_data2.G_out))]])
heat_data_pol.A_out[heat_data_pol.A_out > 0] = 1
heat_data_pol.C_out[heat_data_pol.C_out > 0] = 1
heat_data_pol.G_out[heat_data_pol.G_out > 0] = 1
heat_data_pol.T_out[heat_data_pol.T_out > 0] = 1

heat_data_pol["ancestral"] = ((heat_data_pol.A * heat_data_pol.A_out)  + (heat_data_pol.C * heat_data_pol.C_out) + (heat_data_pol["T"] * heat_data_pol.T_out) + (heat_data_pol.G * heat_data_pol.G_out))
heat_data_pol["derived"] =  (heat_data_pol.A + heat_data_pol.C + heat_data_pol.G + heat_data_pol["T"]) - heat_data_pol.ancestral
piv_data["CE_4n"] = heat_data_pol.derived / (heat_data_pol.ancestral + heat_data_pol.derived) 

path = "/netscratch/dep_mercier/grp_novikova/A.Lyrata/anna_g/" + gene_name + "_CES_dipl_fin.csv"
heat_data2  = pd.read_csv(path, sep=",", header=None)
heat_data2 = heat_data2.rename(columns={0: "position", 1: "A", 2: "C", 3: "G", 4: "T", 5: "A_out", 6: "C_out", 7: "G_out", 8: "T_out"})
heat_data_pol = heat_data2[(heat_data2.A_out == (heat_data2.A_out + heat_data2.C_out + heat_data2.T_out + heat_data2.G_out))]
heat_data_pol = pd.concat([heat_data_pol, heat_data2[(heat_data2.C_out == (heat_data2.A_out + heat_data2.C_out + heat_data2.T_out + heat_data2.G_out))]])
heat_data_pol = pd.concat([heat_data_pol, heat_data2[(heat_data2.G_out == (heat_data2.A_out + heat_data2.C_out + heat_data2.T_out + heat_data2.G_out))]])
heat_data_pol = pd.concat([heat_data_pol, heat_data2[(heat_data2.T_out == (heat_data2.A_out + heat_data2.C_out + heat_data2.T_out + heat_data2.G_out))]])
heat_data_pol.A_out[heat_data_pol.A_out > 0] = 1
heat_data_pol.C_out[heat_data_pol.C_out > 0] = 1
heat_data_pol.G_out[heat_data_pol.G_out > 0] = 1
heat_data_pol.T_out[heat_data_pol.T_out > 0] = 1

heat_data_pol["ancestral"] = ((heat_data_pol.A * heat_data_pol.A_out)  + (heat_data_pol.C * heat_data_pol.C_out) + (heat_data_pol["T"] * heat_data_pol.T_out) + (heat_data_pol.G * heat_data_pol.G_out))
heat_data_pol["derived"] =  (heat_data_pol.A + heat_data_pol.C + heat_data_pol.G + heat_data_pol["T"]) - heat_data_pol.ancestral
piv_data["CS/ES_2n"] = heat_data_pol.derived / (heat_data_pol.ancestral + heat_data_pol.derived) 

path = "/netscratch/dep_mercier/grp_novikova/A.Lyrata/anna_g/" + gene_name + "_PUWS_dipl_fin.csv"
heat_data2  = pd.read_csv(path, sep=",", header=None)
heat_data2 = heat_data2.rename(columns={0: "position", 1: "A", 2: "C", 3: "G", 4: "T", 5: "A_out", 6: "C_out", 7: "G_out", 8: "T_out"})
heat_data_pol = heat_data2[(heat_data2.A_out == (heat_data2.A_out + heat_data2.C_out + heat_data2.T_out + heat_data2.G_out))]
heat_data_pol = pd.concat([heat_data_pol, heat_data2[(heat_data2.C_out == (heat_data2.A_out + heat_data2.C_out + heat_data2.T_out + heat_data2.G_out))]])
heat_data_pol = pd.concat([heat_data_pol, heat_data2[(heat_data2.G_out == (heat_data2.A_out + heat_data2.C_out + heat_data2.T_out + heat_data2.G_out))]])
heat_data_pol = pd.concat([heat_data_pol, heat_data2[(heat_data2.T_out == (heat_data2.A_out + heat_data2.C_out + heat_data2.T_out + heat_data2.G_out))]])
heat_data_pol.A_out[heat_data_pol.A_out > 0] = 1
heat_data_pol.C_out[heat_data_pol.C_out > 0] = 1
heat_data_pol.G_out[heat_data_pol.G_out > 0] = 1
heat_data_pol.T_out[heat_data_pol.T_out > 0] = 1

heat_data_pol["ancestral"] = ((heat_data_pol.A * heat_data_pol.A_out)  + (heat_data_pol.C * heat_data_pol.C_out) + (heat_data_pol["T"] * heat_data_pol.T_out) + (heat_data_pol.G * heat_data_pol.G_out))
heat_data_pol["derived"] =  (heat_data_pol.A + heat_data_pol.C + heat_data_pol.G + heat_data_pol["T"]) - heat_data_pol.ancestral
piv_data["NU/WS_2n"] = heat_data_pol.derived / (heat_data_pol.ancestral + heat_data_pol.derived) 

path = "/netscratch/dep_mercier/grp_novikova/A.Lyrata/anna_g/" + gene_name + "_CES_tetr_fin.csv"
heat_data2  = pd.read_csv(path, sep=",", header=None)
heat_data2 = heat_data2.rename(columns={0: "position", 1: "A", 2: "C", 3: "G", 4: "T", 5: "A_out", 6: "C_out", 7: "G_out", 8: "T_out"})
heat_data_pol = heat_data2[(heat_data2.A_out == (heat_data2.A_out + heat_data2.C_out + heat_data2.T_out + heat_data2.G_out))]
heat_data_pol = pd.concat([heat_data_pol, heat_data2[(heat_data2.C_out == (heat_data2.A_out + heat_data2.C_out + heat_data2.T_out + heat_data2.G_out))]])
heat_data_pol = pd.concat([heat_data_pol, heat_data2[(heat_data2.G_out == (heat_data2.A_out + heat_data2.C_out + heat_data2.T_out + heat_data2.G_out))]])
heat_data_pol = pd.concat([heat_data_pol, heat_data2[(heat_data2.T_out == (heat_data2.A_out + heat_data2.C_out + heat_data2.T_out + heat_data2.G_out))]])
heat_data_pol.A_out[heat_data_pol.A_out > 0] = 1
heat_data_pol.C_out[heat_data_pol.C_out > 0] = 1
heat_data_pol.G_out[heat_data_pol.G_out > 0] = 1
heat_data_pol.T_out[heat_data_pol.T_out > 0] = 1

heat_data_pol["ancestral"] = ((heat_data_pol.A * heat_data_pol.A_out)  + (heat_data_pol.C * heat_data_pol.C_out) + (heat_data_pol["T"] * heat_data_pol.T_out) + (heat_data_pol.G * heat_data_pol.G_out))
heat_data_pol["derived"] =  (heat_data_pol.A + heat_data_pol.C + heat_data_pol.G + heat_data_pol["T"]) - heat_data_pol.ancestral
piv_data["CS_4n"] = heat_data_pol.derived / (heat_data_pol.ancestral + heat_data_pol.derived) 

path = "/netscratch/dep_mercier/grp_novikova/A.Lyrata/anna_g/" + gene_name + "_PUWS_tetr_fin.csv"
heat_data2  = pd.read_csv(path, sep=",", header=None)
heat_data2 = heat_data2.rename(columns={0: "position", 1: "A", 2: "C", 3: "G", 4: "T", 5: "A_out", 6: "C_out", 7: "G_out", 8: "T_out"})
heat_data_pol = heat_data2[(heat_data2.A_out == (heat_data2.A_out + heat_data2.C_out + heat_data2.T_out + heat_data2.G_out))]
heat_data_pol = pd.concat([heat_data_pol, heat_data2[(heat_data2.C_out == (heat_data2.A_out + heat_data2.C_out + heat_data2.T_out + heat_data2.G_out))]])
heat_data_pol = pd.concat([heat_data_pol, heat_data2[(heat_data2.G_out == (heat_data2.A_out + heat_data2.C_out + heat_data2.T_out + heat_data2.G_out))]])
heat_data_pol = pd.concat([heat_data_pol, heat_data2[(heat_data2.T_out == (heat_data2.A_out + heat_data2.C_out + heat_data2.T_out + heat_data2.G_out))]])
heat_data_pol.A_out[heat_data_pol.A_out > 0] = 1
heat_data_pol.C_out[heat_data_pol.C_out > 0] = 1
heat_data_pol.G_out[heat_data_pol.G_out > 0] = 1
heat_data_pol.T_out[heat_data_pol.T_out > 0] = 1

heat_data_pol["ancestral"] = ((heat_data_pol.A * heat_data_pol.A_out)  + (heat_data_pol.C * heat_data_pol.C_out) + (heat_data_pol["T"] * heat_data_pol.T_out) + (heat_data_pol.G * heat_data_pol.G_out))
heat_data_pol["derived"] =  (heat_data_pol.A + heat_data_pol.C + heat_data_pol.G + heat_data_pol["T"]) - heat_data_pol.ancestral
piv_data["NU_4n"] = heat_data_pol.derived / (heat_data_pol.ancestral + heat_data_pol.derived) 

piv_data["scaffold_1, genome position"] = heat_data2.position
filt_data = piv_data[ piv_data.iloc[:,0:6].sum(axis=1) >= 0.03]
filt_data = filt_data[filt_data.iloc[:,0:6].sum(axis=1) <= 5.97]

filt_data.index = filt_data["scaffold_1, genome position"]
filt_data = filt_data.drop(columns="scaffold_1, genome position")

plt.figure(figsize=(18,6), dpi=100)
sns.heatmap(filt_data.T, cmap="viridis")
plt.show()
f = sns.clustermap(filt_data.T, cmap="viridis", col_cluster=False, figsize=(18,10), vmin=0, vmax=1)
plt.title('frequency')
#plt.xlabel("scaffold_7, genome position")
pdfname = gene_name + ".pdf"
f.fig.suptitle(gene_name + " (ZYP1a)", fontsize=20)
plt.show()
f.savefig(pdfname)
pdfname = gene_name + ".jpg"
f.savefig(pdfname)
