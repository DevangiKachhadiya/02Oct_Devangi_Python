try:
    x=10/0
except Exception as e:
    print(f"Error: {e}")
finally:
    print("execution successfully")