from django import forms

class Filter(forms.Form):
    filter = forms.ChoiceField(widget=forms.Select(attrs={'onchange':'this.form.submit()'}), label="Filtrar Por", choices=(("",""),("ods", "Objetivo de Desenvolvimento Social"),("cidade", "Cidade"),("causa", "Causa"), ("estado", "Estado")), initial="")