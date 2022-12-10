# 20221103 - Python - Python OOP - Encapsulation
# 03 - Profile - judge url: https://judge.softuni.org/Contests/Practice/Index/1938#2


class Profile:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if not 5 <= len(value) <= 15:
            raise ValueError(f'The username must be between 5 and 15 characters.')
        self.__username = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        if len(value) < 8 or not any(x.isdigit() for x in value) or not any(x.isalpha() and x == x.upper() for x in value):
            raise ValueError('The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.')
        self.__password = value

    def __str__(self):
        return f'You have a profile with username: "{self.username}" and password: {len(self.__password) * "*"}'


print('\n_______ Test Code 1 _____ uncomment the line bellow to see the error _____\n')
# profile_with_invalid_password = Profile('My_username', 'My-password')


print('\n_______ Test Code 2 _____ uncomment the line bellow to see the error _____\n')
# profile_with_invalid_username = Profile('Too_long_username', 'Any')


print('\n_______ Test Code 3 _______\n')
correct_profile = Profile("Username", "Passw0rd")
print(correct_profile)                                      # You have a profile with username: "Username" and password: ********


print('\n_______ Test Code 4 _____ Prints out all available methods on a specific object ______\n')
all_methods_of_object = dir(Profile)
print('\n'.join([x for x in all_methods_of_object]))
