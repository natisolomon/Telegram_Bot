from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import sqlite3

# Database connection function
def get_students_by_department_and_year(department, year):
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute('SELECT DISTINCT name, phone_number FROM students WHERE department = ? AND year = ?', (department, year))
    result = cursor.fetchall()
    conn.close()
    return result

# Departments and years options
departments = ["Computer Science", "Computer Engineering", "Accounting Degree", "Accounting TVET", "IT"]
years = ["1", "2", "3", "4"]

# Start command to ask for department selection
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    reply_markup = ReplyKeyboardMarkup([[department] for department in departments], one_time_keyboard=True)
    await update.message.reply_text("Welcome! Please select your department:", reply_markup=reply_markup)

# Department selection handler
async def department_selection(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    context.user_data['department'] = update.message.text

    # Ask for year
    reply_markup = ReplyKeyboardMarkup([years], one_time_keyboard=True)
    await update.message.reply_text("Please select your year:", reply_markup=reply_markup)

# Year selection handler and display of student information
async def year_selection(update: Update, context: ContextTypes.DEFAULT_TYPE):
    department = context.user_data.get('department')
    year = update.message.text

    # Fetch student data based on department and year
    students = get_students_by_department_and_year(department, year)

    # Display the data in Telegram
    if students:
        response = f"Students in {department}, Year {year}:\n"
        for student in students:
            name, phone_number = student
            response += f"Name: {name}, Phone: {phone_number}\n"
    else:
        response = f"No students found in {department}, Year {year}."

    await update.message.reply_text(response)

# Main function to set up the bot
def main():
    # Initialize the bot with your token
    application = Application.builder().token("7972502130:AAHqBZnwQIarbDDJACT_9942i_b_t7wSLXA").build()

    # Register handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & filters.Regex(f'^({"|".join(departments)})$'), department_selection))
    application.add_handler(MessageHandler(filters.TEXT & filters.Regex(f'^({"|".join(years)})$'), year_selection))

    # Start the bot
    application.run_polling()

if __name__ == "__main__":
    main()
