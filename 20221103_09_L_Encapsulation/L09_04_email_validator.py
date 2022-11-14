# 20221103 - Python - Python OOP - Encapsulation
# 04 - Email Validator - judge url: https://judge.softuni.org/Contests/Practice/Index/1938#3


class EmailValidator:
    def __init__(self, min_length: int, mail_list: [str], domain_list: [str]):
        self.min_length = min_length
        self.mails = mail_list
        self.domains = domain_list

    def __is_name_valid(self, name: str):
        return len(name) >= self.min_length

    def __is_mail_valid(self, mail):
        return mail in self.mails

    def __is_domain_valid(self, domain):
        return domain in self.domains

    def validate(self, email):
        user_n, domain_ext = email.split('@')
        server, domain = domain_ext.split('.')

        a = self.__is_name_valid(user_n)
        b = self.__is_mail_valid(server)
        c = self.__is_domain_valid(domain)

        return all([a, b, c])


mails = ["gmail", "softuni"]
domains = ["com", "bg"]
email_validator = EmailValidator(6, mails, domains)
print(email_validator.validate("borasam777@gmail.com"))
print(email_validator.validate("borasam777@gmail.net"))
print(email_validator.validate("borasam777@abv.net"))
print(email_validator.validate("bora@gmail.bg"))
