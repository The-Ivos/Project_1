def decorate_message(fun):
    def add_welcome(site_name):
        return "welcome to the"+fun(site_name)+"!"
    
    return add_welcome


@decorate_message
def site(site_name):
    return site_name

print(site("NazdarIvosu.com"))