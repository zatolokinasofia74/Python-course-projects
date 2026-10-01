from datetime import datetime, timezone
import uuid


class Email:
    def __init__(self, sender: "User", receiver: "User", subject: str, body: str):
        self.id = uuid.uuid4().hex[:6]
        self.sender = sender
        self.receiver = receiver
        self.subject = subject
        self.body = body
        self.timestamp = datetime.now(timezone.utc)
        self.is_read = False

    def mark_as_read(self) -> None:
        self.is_read = True

    def display_full(self) -> None:
        self.mark_as_read()
        date_str = self.timestamp.strftime("%Y-%m-%d %H:%M")
        print("\n" + "=" * 45)
        print(f"ID:      {self.id}")
        print(f"From:    {self.sender.name} <{self.sender.address}>")
        print(f"To:      {self.receiver.name} <{self.receiver.address}>")
        print(f"Date:    {date_str}")
        print(f"Subject: {self.subject}")
        print("-" * 45)
        print(self.body)
        print("=" * 45 + "\n")

    def __str__(self) -> str:
        status = "Read" if self.is_read else "Unread"
        date_str = self.timestamp.strftime("%b %d %H:%M")
        return f"[{status:<6}] [{self.id}] From: {self.sender.name:<10} | Subj: {self.subject:<20} | {date_str}"


class MailFolder:
    def __init__(self, name: str):
        self.name = name
        self.emails: list[Email] = []

    def add(self, email: Email) -> None:
        self.emails.append(email)

    def remove(self, index: int) -> Email:
        if not (1 <= index <= len(self.emails)):
            raise IndexError("Message index out of range.")
        return self.emails.pop(index - 1)

    def get(self, index: int) -> Email:
        if not (1 <= index <= len(self.emails)):
            raise IndexError("Message index out of range.")
        return self.emails[index - 1]

    def display(self) -> None:
        print(f"\n--- {self.name.upper()} ({len(self.emails)}) ---")
        if not self.emails:
            print("Folder is empty.")
            return
        for i, email in enumerate(self.emails, start=1):
            print(f"{i:>2}. {email}")

    def __len__(self) -> int:
        return len(self.emails)


class User:
    def __init__(self, name: str, domain: str = "mail.com"):
        self.name = name
        self.address = f"{name.lower().replace(' ', '.')}@{domain}"
        self.folders = {
            "inbox": MailFolder("Inbox"),
            "sent": MailFolder("Sent"),
            "trash": MailFolder("Trash"),
        }

    def _get_folder(self, folder_name: str) -> MailFolder:
        key = folder_name.lower()
        if key not in self.folders:
            raise KeyError(f"Folder '{folder_name}' does not exist.")
        return self.folders[key]

    def send_email(self, receiver: "User", subject: str, body: str) -> Email:
        email = Email(sender=self, receiver=receiver, subject=subject, body=body)
        self.folders["sent"].add(email)
        receiver.receive_email(email)
        print(f"Message sent to {receiver.address}")
        return email

    def receive_email(self, email: Email) -> None:
        self.folders["inbox"].add(email)

    def view_folder(self, folder_name: str = "inbox") -> None:
        try:
            folder = self._get_folder(folder_name)
            folder.display()
        except KeyError as err:
            print(f"Error: {err}")

    def read_email(self, index: int, folder_name: str = "inbox") -> None:
        try:
            folder = self._get_folder(folder_name)
            email = folder.get(index)
            email.display_full()
        except (KeyError, IndexError) as err:
            print(f"Error: {err}")

    def move_to_trash(self, index: int, folder_name: str = "inbox") -> None:
        try:
            folder = self._get_folder(folder_name)
            if folder.name.lower() == "trash":
                print("Error: Message is already in Trash.")
                return
            email = folder.remove(index)
            self.folders["trash"].add(email)
            print(f"Moved '{email.subject}' to Trash.")
        except (KeyError, IndexError) as err:
            print(f"Error: {err}")


def main():
    tory = User("Tory")
    ramy = User("Ramy")

    tory.send_email(ramy, "Meeting Notes", "Here are the notes from today's discussion.")
    ramy.send_email(tory, "Quick Question", "Did you review the database schema yet?")

    ramy.view_folder("inbox")
    ramy.read_email(1)

    tory.view_folder("sent")

    ramy.move_to_trash(1, "inbox")
    ramy.view_folder("trash")
    ramy.view_folder("inbox")


if __name__ == "__main__":
    main()