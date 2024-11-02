from django.db import models

# Create your models here.
class createform(models.Model):
    title=models.CharField(max_length=1234),
    discription=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)




class Question(models.Model):
    TEXT = 'text'
    MULTIPLE_CHOICE = 'multiple_choice'
    CHECKBOX = 'checkbox'
    DATE = 'date'
    FIELD_TYPES = [
        (TEXT, 'Text'),
        (MULTIPLE_CHOICE, 'Multiple Choice'),
        (CHECKBOX, 'Checkbox'),
        (DATE, 'Date'),
    ]

    form = models.ForeignKey(createform, related_name='questions', on_delete=models.CASCADE)
    question_text = models.CharField(max_length=255)
    field_type = models.CharField(max_length=20, choices=FIELD_TYPES, default=TEXT)
    is_required = models.BooleanField(default=True)

    def __str__(self):
        return self.question_text

# class Choice(models.Model):
#     question = models.ForeignKey(Question, related_name='choices', on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=100)

#     def __str__(self):
#         return self.choice_text

# class Answer(models.Model):
#     question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
#     form_response_id = models.CharField(max_length=255)  # to group answers by form submission
#     answer_text = models.TextField(blank=True, null=True)
#     selected_choice = models.ForeignKey(Choice, related_name='answers', on_delete=models.SET_NULL, null=True, blank=True)

#     def __str__(self):
#         return f"Answer to {self.question}"
