setwd('/netscratch/dep_mercier/grp_novikova/A.Lyrata/map_feb23_to_NT1/nquire')

data<-read.table('lrmodel_output_denoised_clean1.txt', header=T)

PL<-c()
for (i in 1:dim(data)[1]){
  name<-unlist(strsplit(as.character(data$file[i]), split='/'))[8]
  pl<-which(data[i,3:5]==max(data[i,3:5]))+1
  PL<-rbind(PL, c(name, pl))
}

write.table(file='inferred_ploidy.txt', data.frame(PL),
            quote = F, sep = "\t",
            eol = "\n", na = "NA", dec = ".", row.names = F,
            col.names = TRUE,)
