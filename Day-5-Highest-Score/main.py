
student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 99, 105]

maxscore = 0
for score in student_scores:
    if score > maxscore:
        maxscore = score
print(maxscore)
