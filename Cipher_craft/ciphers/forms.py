from django import forms


class CipherTextForm(forms.Form):
    text = forms.CharField(
        label='Text', 
        max_length=1000
    )
    key = forms.IntegerField(
        label='Key',
        required=False,
        initial=1,
    )
    operation = forms.ChoiceField(
        label='Encrypt or Decrypt',
        choices=(
            ('encrypt', "Encrypt"),
            ('decrypt', "Decrypt"),
        )
    )
    
class VigenereForm(forms.Form):
    text = forms.CharField(
        label='Text', 
        max_length=1000
    )
    key = forms.CharField(
        label='Key', 
        required=True,
        max_length=1000
    )
    operation = forms.ChoiceField(
        label='Encrypt or Decrypt',
        choices=(
            ('encrypt', "Encrypt"),
            ('decrypt', "Decrypt"),
        )
    )
    
class MorseForm(forms.Form):
    text = forms.CharField(
        label='Text', 
        max_length=1000
    )
    operation = forms.ChoiceField(
        label='Encrypt or Decrypt',
        choices=(
            ('encrypt', "Encrypt"),
            ('decrypt', "Decrypt"),
        )
    ) 

class TowerOfHanoiForm(forms.Form):
    disks = forms.IntegerField(
        label='Key',
        required=False,
        initial=1,
    )
    operation = forms.ChoiceField(
        label='Choice',
        choices=(
            ('decrypt', "Decrypt"),
        )
    )


class XOR(forms.Form):
    text = forms.CharField(
        label='Text',
        max_length=1000
    )
    key = forms.CharField(
        label='Key',
        required=False,
        initial='P',
    )
    operation = forms.ChoiceField(
        label='Encrypt or Decrypt',
        choices=(
            ('encrypt', "Encrypt"),
            ('decrypt', "Decrypt"),
        )
    )

class atbash(forms.Form):
    text = forms.CharField(
        label='Text',
        max_length=1000
    )
    operation = forms.ChoiceField(
        label='Encrypt or Decrypt',
        choices=(
            ('encrypt', "Encrypt"),
            ('decrypt', "Decrypt"),
        )
    )