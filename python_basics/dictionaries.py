me = {
    'name': 'Isaac',
    'age': 24,
    'country': 'The United States',
    'language': 'unknown'
}
def aboutMe():
    print """
    My name is %s
    My age is %s
    My country of birth is %s
    My favorite language is %s
    """ % (me['name'], me['age'], me['country'], me['language'])
aboutMe()