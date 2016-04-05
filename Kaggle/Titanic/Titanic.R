trainData <- read.csv("train.csv",header = TRUE)
teD <- read.csv("test.csv",header = TRUE)
names(trainData)
trainData$Sex
Sexd <- rep(nrow(trainData),0)
Sexd[trainData$Sex == "female"] <- 0
Sexd[trainData$Sex == "male"] <- 1
Sexd
trainData$Survived
lifit <- lm(Survived~Sex+Age+Fare+Parch,trainData)
summary(lifit)
coef(lifit)
ans <- predict(lifit,data.frame(Sex=teD$Sex,Age=teD$Age,Fare=teD$Fare,Parch=teD$Parch))
output <- rep(nrow(teD),0)
output[ans >0.5] <- 1
output[ans <0.5] <- 0
output[is.na(ans)] <- 0
output
subFile <- data.frame(PassengerId=teD$PassengerId,Survived = output)
subFile
write.csv(subFile,file="submit.csv",row.names = F,quote = F)
