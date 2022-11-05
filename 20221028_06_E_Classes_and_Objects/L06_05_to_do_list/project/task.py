class Task:
    def __init__(self, name: str, due_date: str):
        self.name = name
        self.due_date = due_date
        self.comments = []
        self.completed = False

    def change_name(self, new_name: str):
        if new_name == self.name:
            return f'Name cannot be the same.'
        self.name = new_name
        return self.name

    def change_due_date(self, new_dew_date: str):
        if new_dew_date == self.due_date:
            return f'Date cannot be the same.'
        self.due_date = new_dew_date
        return self.due_date

    def add_comment(self, comment: str):
        self.comments.append(comment)

    def edit_comment(self, comment_number: int, new_comment: str):
        if not 0 <= comment_number < len(self.comments):
            return f'Cannot find comment.'

        self.comments[comment_number] = new_comment

        comments_list = ', '.join(self.comments)
        return comments_list

    def details(self):
        return f'Name: {self.name} - Due Date: {self.due_date}'
