# 🕑 Reminder CLI App by Zohair Ahmed

A simple command-line based Python reminder application that uses `plyer` to show desktop notifications at user-defined times.

## ✅ Features

- Add multiple reminders with specific times
- View currently set reminders
- Notifies you with a system popup when it's time
- Easy-to-use menu in the terminal

## 💻 How It Works

1. You can **add a reminder** by entering your message and the time (in `HH:MM` format).
2. You can **view all saved reminders**.
3. After you exit the menu, the app will continue to **check the time every 30 seconds** and notify you when the time matches your reminder.

## 📦 Requirements

- Python 3
- `plyer` for desktop notifications

### Install dependencies

```bash
pip install plyer
```

## 🛠️ Usage

Run the script:

```bash
python reminder.py
```

You'll be presented with a simple menu:

```text
1. Add reminder
2. View reminders
3. Exit
```

When it's time, a system notification will pop up with your message. Example:

> 🔔 "**Reminder:** Take a break!"  

## ⚙️ Notification Customization

The icon for the notification can be customized by replacing the path in:

```python
app_icon = r"D:\python projects\reminder\reminder.ico"
```

Replace it with the path to your `.ico` file, or set it to `None` if you want no icon.

## 📌 Example

```text
What do you want to be reminded of? Drink water
When do you want to be reminded? (Hour:MM) 14:30
Reminder added successfully!
```

## 🚧 Known Limitations

- Time input must be in `HH:MM` format (24-hour clock).
- The app must remain running to trigger notifications.
- It checks every 30 seconds — might miss a reminder by a few seconds.

## 👨‍💻 Author

Created by [Zohair Ahmed](https://github.com/zohair-ahmed-nadeem) — feel free to contribute or suggest improvements!

## 📝 License

This project is licensed under the MIT License.
