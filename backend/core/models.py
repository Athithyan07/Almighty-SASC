from django.db import models


class StudentMark(models.Model):
    # student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='marks')
    subject1_marks = models.IntegerField()
    subject2_marks = models.IntegerField()
    subject3_marks = models.IntegerField()
    subject4_marks = models.IntegerField()
    subject5_marks = models.IntegerField()
    subject6_marks = models.IntegerField()
    total_marks = models.IntegerField(blank=True, null=True)
    grade = models.CharField(max_length=10, blank=True, null=True)
    recorded_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.total_marks = (self.subject1_marks + self.subject2_marks +
                            self.subject3_marks + self.subject4_marks +
                            self.subject5_marks + self.subject6_marks)
        # Simple grading logic, can be expanded
        if self.total_marks >= 500:
            self.grade = 'A+'
        elif self.total_marks >= 400:
            self.grade = 'A'
        elif self.total_marks >= 300:
            self.grade = 'B'
        elif self.total_marks >= 200:
            self.grade = 'C'
        else:
            self.grade = 'F'
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Student's marks"

class StudentAttendance(models.Model):
    # student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='attendance')
    date = models.DateField()
    is_present = models.BooleanField(default=False)
    # recorded_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='recorded_attendances')
    recorded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # unique_together = ('student', 'date')
        pass

    def __str__(self):
        return f"Attendance - {self.date} - {'Present' if self.is_present else 'Absent'}"

class ChatMessage(models.Model):
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['timestamp']

    def __str__(self):
        return f"Message at {self.timestamp}"
