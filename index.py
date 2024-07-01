import tkinter as tk
from tkinter import messagebox

existing_reviews = []

def upload_review():
    restaurant_name = entry_name.get()
    review_text = text_review.get("1.0", tk.END).strip()
    rating = stars.get()
    address = entry_address.get()

    if not restaurant_name or not review_text or not rating or not address:
        messagebox.showwarning("Input Error", "कृपया अपनी समीक्षा दें.")
        return

    # Here you can process the review, e.g., save it to a file or database
    new_review = {
        "restaurant_name": restaurant_name,
        "review": review_text,
        "rating": rating,
        "address": address
    }
    existing_reviews.append(new_review)

    # Display success message
    messagebox.showinfo("Review Submitted", "Review submitted successfully!")

    # Reset fields
    entry_name.delete(0, tk.END)
    text_review.delete("1.0", tk.END)
    stars.set(0)
    entry_address.delete(0, tk.END)

    # Update the view after submission
    view_reviews()

def remove_review(index):
    del existing_reviews[index]
    messagebox.showinfo("Review Removed", "Review removed successfully!")
    view_reviews()

def view_reviews():
    # Create or update the review window
    if 'review_window' in globals() and isinstance(review_window, tk.Toplevel) and review_window.winfo_exists():
        review_window.destroy()

    review_window = tk.Toplevel(root)
    review_window.title("Existing Reviews")

    if existing_reviews:
        for i, review in enumerate(existing_reviews):
            review_frame = tk.Frame(review_window, padx=10, pady=10)
            review_frame.grid(row=i, column=0, padx=10, pady=10)

            tk.Label(review_frame, text=f"Restaurant: {review['restaurant_name']}").grid(row=0, column=0, sticky="w")
            tk.Label(review_frame, text=f"Review: {review['review']}").grid(row=1, column=0, sticky="w")
            tk.Label(review_frame, text=f"Rating: {review['rating']} Stars").grid(row=2, column=0, sticky="w")
            tk.Label(review_frame, text=f"Address: {review['address']}").grid(row=3, column=0, sticky="w")

            # Button to remove the review
            remove_button = tk.Button(review_frame, text="Remove Review", command=lambda idx=i: remove_review(idx))
            remove_button.grid(row=4, column=0, pady=5)

    else:
        tk.Label(review_window, text="No reviews yet.").pack(padx=20, pady=20)

# Main tkinter window
root = tk.Tk()
root.title("Restaurant Review")

#  Name for restraunt
label_name = tk.Label(root, text="Restaurant Name:")
label_name.grid(row=0, column=0, padx=10, pady=10)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1, padx=10, pady=10)


label_review = tk.Label(root, text="Review:")
label_review.grid(row=1, column=0, padx=10, pady=10)
text_review = tk.Text(root, height=5, width=50)
text_review.grid(row=1, column=1, padx=10, pady=10)

# 1-5 rating
stars = tk.IntVar()
rating_label = tk.Label(root, text="Rating:")
rating_label.grid(row=2, column=0, padx=10, pady=10)
for i in range(1, 6):
    rb = tk.Radiobutton(root, text=f"{i} Star{'s' if i > 1 else ''}", variable=stars, value=i)
    rb.grid(row=2, column=i, padx=5, pady=10)

# for adress
label_address = tk.Label(root, text="Address:")
label_address.grid(row=3, column=0, padx=10, pady=10)
entry_address = tk.Entry(root)
entry_address.grid(row=3, column=1, padx=10, pady=10)

# submit review
submit_button = tk.Button(root, text="Submit Review", command=upload_review)
submit_button.grid(row=4, column=0, padx=10, pady=10)
view_button = tk.Button(root, text="View Existing Reviews", command=view_reviews)
view_button.grid(row=4, column=1, padx=10, pady=10)

# Start main loop
root.mainloop()
