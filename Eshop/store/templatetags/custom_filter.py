from django import template

register = template.Library()                           

@register.filter(name = 'currency')                   #rupee symbol sign concatination kyuki template mathematical operation ya concatination nhi hoga   
def currency(number):                         
    return "Rs." + str(number)

@register.filter(name = 'multiply')
def multiply(number, number1):
    return number * number1