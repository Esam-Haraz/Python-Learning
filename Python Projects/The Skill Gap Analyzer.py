senior_skills = {"HTML", "CSS", "JS", "Python", "Django", "Docker", "AWS"}
junior_skills = {"HTML", "CSS", "JS", "React", "Git"}
print("Shared Skills: {}".format(senior_skills.intersection(junior_skills)))
print("Skills Junior Needs: {}".format(senior_skills.difference(junior_skills)))
print("Skills Senior Lacks: {}".format(junior_skills.difference(senior_skills)))
print("Total Team Skills: {}".format(senior_skills.union(junior_skills)))