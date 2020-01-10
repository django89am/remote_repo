from django import forms

class StudentDataForm(forms.Form):
    student_name=forms.CharField(
        label="Name ",
        widget=forms.TextInput(
            attrs={
                'placeholder':'Student Name',
                'class':'form-control'
            }
        )
    )
    course_name = forms.CharField(
        label="Course ",
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Course Name',
                'class': 'form-control'
            }
        )
    )
    course_fee = forms.IntegerField(
        label="Fee ",
        widget=forms.NumberInput(
            attrs={
                'placeholder': 'Course Fee',
                'class': 'form-control'
            }
        )
    )
    institute_name = forms.CharField(
        label="Institue ",
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Institute Name',
                'class': 'form-control'
            }
        )
    )
    qualification = forms.CharField(
        label="Qualification ",
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Qualification',
                'class': 'form-control'
            }
        )
    )
    location_name = forms.CharField(
        label="Location ",
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Location',
                'class': 'form-control'
            }
        )
    )


