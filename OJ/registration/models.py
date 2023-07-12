from django.db import models
from django.contrib.auth.models import User


class Problem(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    difficulty = models.CharField(max_length=20)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title



class Submission(models.Model):
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.TextField()
    language = models.CharField(max_length=50)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.problem.title}"
    


class TestCase(models.Model):
    problem = models.ForeignKey('Problem', on_delete=models.CASCADE)
    input_data = models.TextField()
    expected_output = models.TextField()

    def __str__(self):
        return f"TestCase for Problem {self.problem_id}"




class Result(models.Model):
    submission = models.ForeignKey('Submission', on_delete=models.CASCADE)
    test_case = models.ForeignKey(TestCase, on_delete=models.CASCADE)
    actual_output = models.TextField()
    is_passed = models.BooleanField()

    def __str__(self):
        return f"Result for Submission {self.submission_id} and TestCase {self.test_case_id}"
