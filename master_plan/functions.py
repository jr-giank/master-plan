def is_admin(user):

    if user.is_authenticated == True and user.role == 'A':
        return True
        
    return False