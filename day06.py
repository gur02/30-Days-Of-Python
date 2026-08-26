attendance_percentage = 82
has_completed_assignment = True
has_outstanding_fess = False
if attendance_percentage >= 75 and has_completed_assignment == True:
    print("Exam status: Eligible! Hall ticket generated.")
else:
    print("Emam status: Not Eligible! Check attendance or assignment.")
if has_outstanding_fess == True or not has_completed_assignment:
    print("Account Status: Alert! Please visit the college administrative office.")
else:
    print("Accont Status: All clear! No administration alerts.")
