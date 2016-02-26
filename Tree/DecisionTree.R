# load the data set
load("SampleData_Bank")

#calculate the entropy
cal_entropy <- function(Data){
  h <- 0
  amount <- length(Data)
  #size of possible value
  value_op <- unique(Data)
  value_ops <- length(value_op)
  for(i in 1:value_ops){
    temp <- length(Data[Data==value_op[i]])/amount
    temp <- temp*log2(temp)
    h <- h+temp
  }
  return (-h)
}
# to define the struct of tree using list
# label is the split var of current node, firstchild is the ID of the first child node of current node.
#nochildren is the amount of current node's children.type define the current node is leaf or inner.
tre <- list(label <- array(),class <- array(),firstchild <- array(),nochildren <- array(),father <- array(), type <- array())
#The amount of node in this tree.
node_size <- 1;

#create node of decision
create_node <- function(Data){
  var_amount <- length(Data)
  if(is.atomic(Data)==TRUE){ var_amount <- 0}
  if(var_amount == 1){
    #No var to split this node.
    tre$label[node_size] <<- which.max(table(Data[,var_amount]))
    tre$type[node_size] <<- "leaf"
    tre$nochildren <<- 0L
    node_size <<- node_size +1
  }else{
    
    #Remain obs. are in the same class.
    if(length(unique(Data[,var_amount]))==1){
      #Leaf node
      tre$class[node_size] <<- Data[1,var_amount]
      tre$type[node_size] <<- "leaf"
      tre$nochildren[node_size] <<- 0L
      node_size <<- node_size +1
    }else{
      #To calculate the entropy of current data set of.
      #The default column of class is the last one(Data[,var_amount]).
      entropy <- cal_entropy(Data[,var_amount])
      varname <- colnames(Data)
      cat("Entropy:",entropy)
      
      #To calculate Info Gain
      IG <- array()
      size <- nrow(Data)
      for(i in 1:(var_amount-1) ){
        value_op <- unique(unlist(Data[varname[i]]))
        value_ops <- length(value_op)
        sument <- 0
        for(j in 1:value_ops){
          tempset <- subset(Data,Data[[varname[i]]]==value_op[j],select=varname[var_amount])  
          subsize <- length(tempset[,1])
          entropy_v <- cal_entropy(tempset[,1])
          sument <- sument +entropy_v*subsize/size
        }
        IG[i] <- entropy - sument
        cat("IG: ",varname[i]," ",IG[i],"\n")

      }
      #decide which var we use to split the node
      cat("node split by",varname[which.max(IG)],"\n")
      tre$label[node_size] <<- paste(tre$label[node_size]," split by ",toString(varname[which.max(IG)]))
      tre$class[node_size] <<- "NULL"
      tre$firstchild[node_size] <<- node_size+1
      tre$nochildren[node_size] <<- 0
      tre$type[node_size] <<- "inner"
      fa <- node_size
      temp <- which.max(IG)

      node_size <<- node_size+1
      for(i in 1:value_ops){
        if(nrow(subset(Data,Data[[varname[temp]]]==value_op[i],select= -temp ))!=0){
        tre$nochildren[fa] <<- tre$nochildren[fa] + 1
        tre$father[fa+tre$nochildren[fa]] <<- fa
        tre$label[fa+tre$nochildren[fa]] <<- paste("Attr  ",varname[temp],value_op[i])
        create_node(subset(Data,Data[[varname[temp]]]==value_op[i],select= -temp ))
        }
      }
    }
    
  }
}

create_node(Bankruptcy)
