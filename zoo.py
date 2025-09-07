import streamlit as st
import sqlite3

# Database Setup
def init_db():
    conn = sqlite3.connect("zoo.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS animals (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 name TEXT, 
                 species TEXT, 
                 age INTEGER, 
                 health_status TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS staff (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 name TEXT, 
                 role TEXT, 
                 experience INTEGER)''')
    c.execute('''CREATE TABLE IF NOT EXISTS visitors (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 name TEXT, 
                 ticket_type TEXT)''')
    conn.commit()
    conn.close()

# Function to Add Data
def add_animal(name, species, age, health_status):
    conn = sqlite3.connect("zoo.db")
    c = conn.cursor()
    c.execute("INSERT INTO animals (name, species, age, health_status) VALUES (?, ?, ?, ?)",
              (name, species, age, health_status))
    conn.commit()
    conn.close()

def add_staff(name, role, experience):
    conn = sqlite3.connect("zoo.db")
    c = conn.cursor()
    c.execute("INSERT INTO staff (name, role, experience) VALUES (?, ?, ?)", (name, role, experience))
    conn.commit()
    conn.close()

def add_visitor(name, ticket_type):
    conn = sqlite3.connect("zoo.db")
    c = conn.cursor()
    c.execute("INSERT INTO visitors (name, ticket_type) VALUES (?, ?)", (name, ticket_type))
    conn.commit()
    conn.close()

# Function to View Data
def view_data(table):
    conn = sqlite3.connect("zoo.db")
    c = conn.cursor()
    c.execute(f"SELECT * FROM {table}")
    data = c.fetchall()
    conn.close()
    return data

# Streamlit UI
st.title("🐘 Zoo Management System")

menu = ["Add Animal", "View Animals", "Add Staff", "View Staff", "Add Visitor", "View Visitors"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Add Animal":
    st.subheader("Add New Animal")
    name = st.text_input("Animal Name")
    species = st.text_input("Species")
    age = st.number_input("Age", min_value=0)
    health_status = st.selectbox("Health Status", ["Healthy", "Sick", "Under Treatment"])
    if st.button("Add Animal"):
        add_animal(name, species, age, health_status)
        st.success(f"Added {name} to the zoo.")

elif choice == "View Animals":
    st.subheader("List of Animals")
    animals = view_data("animals")
    for animal in animals:
        st.text(f"{animal[1]} - {animal[2]}, Age: {animal[3]}, Health: {animal[4]}")

elif choice == "Add Staff":
    st.subheader("Add New Staff Member")
    name = st.text_input("Staff Name")
    role = st.text_input("Role")
    experience = st.number_input("Years of Experience", min_value=0)
    if st.button("Add Staff"):
        add_staff(name, role, experience)
        st.success(f"Added {name} to staff.")

elif choice == "View Staff":
    st.subheader("List of Staff Members")
    staff = view_data("staff")
    for member in staff:
        st.text(f"{member[1]} - {member[2]}, Experience: {member[3]} years")

elif choice == "Add Visitor":
    st.subheader("Add New Visitor")
    name = st.text_input("Visitor Name")
    ticket_type = st.selectbox("Ticket Type", ["Regular", "VIP", "Child"])
    if st.button("Add Visitor"):
        add_visitor(name, ticket_type)
        st.success(f"Added {name} as a visitor.")

elif choice == "View Visitors":
    st.subheader("List of Visitors")
    visitors = view_data("visitors")
    for visitor in visitors:
        st.text(f"{visitor[1]} - Ticket: {visitor[2]}")

# Initialize Database on First Run
init_db()

