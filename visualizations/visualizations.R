transfers = read.csv("transfers2.csv", stringsAsFactors=FALSE)
age1 = as.numeric(transfers$Age)
age = c()
for (i in 1:length(age1)) {
	if (!is.na(age1[i])) {
		age = c(age, age1[i])
	}
}
hist(age)

position = transfers$Position

# posCnt holds a count of positions in the data set as follows:
# posCnt[1] holds count of goal keepers
# posCnt[2] holds count of defenders
# posCnt[3] holds count of midfielders (CAM, CDM, LM, RM)
# posCnt[4] holds count of wingers
# posCnt[5] holds count of strikers
posCnt = rep(0, 5) # Counts for each position
for (i in 1:length(position)) {
	if (position[i] == "GK") {
		posCnt[1] = posCnt[1] + 1
	}
	else if (position[i] == "LB" || position[i] == "RB" ||
		position[i] == "CB" || position[i] == "Defender") {
		posCnt[2] = posCnt[2] + 1
	}
	else if (position[i] == "CM" || position[i] == "DM" ||
		position[i] == "AM" || position[i] == "Midfielder") {
		posCnt[3] = posCnt[3] + 1
	}
	else if (position[i] == "LW" || position[i] == "RW" ||
		position[i] == "LM" || position[i] == "RM") {
		posCnt[4] = posCnt[4] + 1
	}
	else if (position[i] == "CF" || position[i] == "Striker" ||
		position[i] == "SS") {
		posCnt[5] = posCnt[5] + 1
	}
	else {
		print(position[i])
	}
}
# posCnt
# sum(posCnt)
# p = table(position)
# p[names(p)==" GK"] # Count of a certain position

# barplot(posCnt, main="Distribution of Positions", 
# 	xlab="Position", ylab="Count")