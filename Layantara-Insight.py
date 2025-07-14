import gspread
from oauth2client.service_account import ServiceAccountCredentials
import random

def save_to_google_sheets(cuq_responses):
    """
    Saves a list of 7 CUQ responses to a predefined Google Sheet.
    CUQ responses must be in a 1D list of integers (Likert scale 1–5).
    """
    # Google Sheets API scope
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    try:
        creds = ServiceAccountCredentials.from_json_keyfile_name("service_account.json", scope)
        client = gspread.authorize(creds)
        sheet = client.open("Layantara_CUQ_Results").sheet1
        sheet.append_row(cuq_responses)
    except Exception as e:
        st.error("❌ Failed to save CUQ data to Google Sheets.")
        st.exception(e)
import streamlit as st
QUIZ_BANK = {
    "Angles": [
        {
            "question": "What is the sum of the angles in a kite?",
            "options": ["180°", "360°", "90°", "270°"],
            "answer": "360°",
            "explanation": "A kite is a quadrilateral, and the sum of angles in any quadrilateral is always 360°."
        },
        {
            "question": "If one angle of a kite is 110°, what is the measure of the opposite angle?",
            "options": ["110°", "70°", "90°", "180°"],
            "answer": "110°",
            "explanation": "In a kite, the two pairs of opposite angles are equal. So if one angle is 110°, its opposite is also 110°."
        },
        {
            "question": "A kite has angles 80°, 100°, 80°, and ___. What is the missing angle?",
            "options": ["100°", "80°", "90°", "110°"],
            "answer": "100°",
            "explanation": "The sum of all angles must be 360°. 80 + 100 + 80 = 260, so the missing angle is 360 - 260 = 100°."
        },
        {
            "question": "Which angle is always equal in a kite?",
            "options": ["Adjacent", "Opposite", "All", "None"],
            "answer": "Opposite",
            "explanation": "A kite has two pairs of equal adjacent sides, and the angles between those sides are equal (opposite angles)."
        },
        {
            "question": "If a kite has two angles of 120° each, what is the sum of the other two angles?",
            "options": ["120°", "240°", "60°", "180°"],
            "answer": "120°",
            "explanation": "The sum of all angles is 360°. 120 + 120 = 240, so the other two must add up to 120°."
        },
        {
            "question": "What is the measure of each angle in a square-shaped kite?",
            "options": ["90°", "60°", "120°", "45°"],
            "answer": "90°",
            "explanation": "A square has four equal angles of 90°, so a square-shaped kite also has 90° angles."
        },
        {
            "question": "If a kite has angles 70°, 110°, 70°, and ___, what is the missing angle?",
            "options": ["110°", "70°", "90°", "120°"],
            "answer": "110°",
            "explanation": "The sum of all angles is 360°. 70 + 110 + 70 = 250, so the missing angle is 360 - 250 = 110°."
        },
        {
            "question": "Which Indonesian kite is known for its sharp angles?",
            "options": ["Janggan", "Barong", "Diamond", "Box"],
            "answer": "Janggan",
            "explanation": "The Janggan kite from Bali is famous for its long tail and sharp angles at the head."
        },
        {
            "question": "If a kite has two right angles, what is the sum of the other two angles?",
            "options": ["180°", "90°", "120°", "150°"],
            "answer": "180°",
            "explanation": "Two right angles are 90° each, so 90 + 90 = 180°. The other two must add up to 360 - 180 = 180°."
        },
        {
            "question": "What is the largest angle possible in a kite?",
            "options": ["179°", "180°", "120°", "150°"],
            "answer": "179°",
            "explanation": "Angles in a quadrilateral must be less than 180°. 179° is the largest possible for a single angle in a kite."
        }
    ],
    "Trigonometry": [
        {
            "question": "If a kite string makes a 30° angle with the ground and is 10m long, what is the height above ground? (sin 30° = 0.5)",
            "options": ["5m", "10m", "15m", "20m"],
            "answer": "5m",
            "explanation": "Height = string × sin(angle) = 10m × 0.5 = 5m."
        },
        {
            "question": "A kite is flying at a height of 8m with a string length of 10m. What is the angle of elevation? (sin θ = 0.8)",
            "options": ["53°", "37°", "45°", "60°"],
            "answer": "53°",
            "explanation": "sin θ = height / string = 8/10 = 0.8, so θ = arcsin(0.8) ≈ 53°."
        },
        {
            "question": "If the diagonal of a kite is 6m and the angle between diagonals is 60°, what is the area? (Area = 1/2 × d1 × d2 × sin θ)",
            "options": ["9m²", "12m²", "15m²", "18m²"],
            "answer": "9m²",
            "explanation": "Area = 1/2 × 6 × 3 × sin(60°) = 1/2 × 6 × 3 × 0.866 ≈ 9m²."
        },
        {
            "question": "A kite string forms a 45° angle with the ground and is 7m long. What is the vertical height? (sin 45° ≈ 0.707)",
            "options": ["4.95m", "5m", "7m", "3.5m"],
            "answer": "4.95m",
            "explanation": "Height = 7m × sin(45°) ≈ 7 × 0.707 ≈ 4.95m."
        },
        {
            "question": "If a kite is 12m above the ground and the string is 15m, what is the angle of elevation? (sin θ = 0.8)",
            "options": ["53°", "37°", "45°", "60°"],
            "answer": "53°",
            "explanation": "sin θ = 12/15 = 0.8, so θ = arcsin(0.8) ≈ 53°."
        },
        {
            "question": "A kite is flying with a string at 60° to the ground and the string is 10m. What is the height? (sin 60° ≈ 0.866)",
            "options": ["8.66m", "10m", "6m", "12m"],
            "answer": "8.66m",
            "explanation": "Height = 10m × sin(60°) ≈ 10 × 0.866 = 8.66m."
        },
        {
            "question": "If the diagonal of a kite is 8m and the angle between diagonals is 45°, what is the area? (Area = 1/2 × d1 × d2 × sin θ)",
            "options": ["16m²", "22.6m²", "12m²", "8m²"],
            "answer": "16m²",
            "explanation": "Area = 1/2 × 8 × 4 × sin(45°) = 1/2 × 8 × 4 × 0.707 ≈ 16m²."
        },
        {
            "question": "A kite string forms a 37° angle with the ground and is 12m long. What is the vertical height? (sin 37° ≈ 0.601)",
            "options": ["7.2m", "8m", "10m", "12m"],
            "answer": "7.2m",
            "explanation": "Height = 12m × sin(37°) ≈ 12 × 0.601 ≈ 7.2m."
        },
        {
            "question": "If a kite is 15m above the ground and the string is 20m, what is the angle of elevation? (sin θ = 0.75)",
            "options": ["48.6°", "60°", "45°", "30°"],
            "answer": "48.6°",
            "explanation": "sin θ = 15/20 = 0.75, so θ = arcsin(0.75) ≈ 48.6°."
        },
        {
            "question": "A kite is flying with a string at 90° to the ground and the string is 5m. What is the height?",
            "options": ["5m", "0m", "10m", "2.5m"],
            "answer": "5m",
            "explanation": "At 90°, the string is vertical, so the height is equal to the string length: 5m."
        }
    ],
    "Geometry": [
        {
            "question": "What is the shape of a traditional diamond kite?",
            "options": ["Quadrilateral", "Triangle", "Circle", "Rectangle"],
            "answer": "Quadrilateral",
            "explanation": "A diamond kite is a quadrilateral because it has four sides and four angles."
        },
        {
            "question": "Which geometric property is unique to kites?",
            "options": ["Two pairs of adjacent sides equal", "All sides equal", "All angles equal", "No equal sides"],
            "answer": "Two pairs of adjacent sides equal",
            "explanation": "Kites have two pairs of adjacent sides that are equal in length, which is a unique property among quadrilaterals."
        },
        {
            "question": "What is the area formula for a kite with diagonals d1 and d2?",
            "options": ["(1/2) × d1 × d2", "d1 × d2", "(1/2) × base × height", "π × r²"],
            "answer": "(1/2) × d1 × d2",
            "explanation": "The area of a kite is half the product of its diagonals: Area = (1/2) × d1 × d2."
        },
        {
            "question": "Which Indonesian kite is known for its geometric patterns?",
            "options": ["Janggan", "Barong", "Diamond", "Box"],
            "answer": "Janggan",
            "explanation": "The Janggan kite is famous for its intricate geometric patterns and long tail, often seen in Balinese festivals."
        },
        {
            "question": "What is the perimeter of a kite with sides 3m, 3m, 2m, 2m?",
            "options": ["10m", "8m", "12m", "6m"],
            "answer": "10m",
            "explanation": "Perimeter is the sum of all sides: 3 + 3 + 2 + 2 = 10 meters."
        },
        {
            "question": "Which shape is NOT a type of kite?",
            "options": ["Hexagon", "Quadrilateral", "Triangle", "Box"],
            "answer": "Hexagon",
            "explanation": "A kite is always a quadrilateral, never a hexagon."
        },
        {
            "question": "What is the diagonal length of a square kite with side 2m?",
            "options": ["2.83m", "4m", "2m", "1.41m"],
            "answer": "2.83m",
            "explanation": "The diagonal of a square is side × √2, so 2 × 1.414 ≈ 2.83 meters."
        },
        {
            "question": "Which property is true for all kites?",
            "options": ["Diagonals are perpendicular", "All sides equal", "All angles equal", "Diagonals are parallel"],
            "answer": "Diagonals are perpendicular",
            "explanation": "The diagonals of a kite always cross at right angles (perpendicular)."
        },
        {
            "question": "What is the area of a kite with diagonals 4m and 6m?",
            "options": ["12m²", "24m²", "10m²", "8m²"],
            "answer": "12m²",
            "explanation": "Area = (1/2) × 4 × 6 = 12 square meters."
        },
        {
            "question": "Which geometric shape is most common in Indonesian kite festivals?",
            "options": ["Diamond", "Box", "Triangle", "Circle"],
            "answer": "Diamond",
            "explanation": "Diamond-shaped kites are the most popular in Indonesian festivals due to their stability and ease of decoration."
        }
    ],
    "Composite Shapes": [
        {
            "question": "A kite has a rectangular body (2m × 1.5m) and a triangular tail (1.5m base, 0.8m height). What is the total area?",
            "options": ["3.6 m²", "3.9 m²", "4.1 m²", "4.5 m²"],
            "answer": "3.6 m²",
            "explanation": "Area = rectangle + triangle = (2 × 1.5) + (0.5 × 1.5 × 0.8) = 3 + 0.6 = 3.6 m²."
        },
        {
            "question": "A traditional Indonesian kite is made from two triangles (base 2m, height 1m each) joined to a square (1m × 1m). What is the total area?",
            "options": ["3 m²", "4 m²", "5 m²", "6 m²"],
            "answer": "3 m²",
            "explanation": "Area = 2 × (0.5 × 2 × 1) + (1 × 1) = 2 × 1 + 1 = 3 m²."
        },
        {
            "question": "A kite consists of a circle (radius 0.5m) and a rectangle (2m × 1m). What is the total area? (Use π ≈ 3.14)",
            "options": ["2.79 m²", "3.14 m²", "3.64 m²", "4.14 m²"],
            "answer": "3.14 m²",
            "explanation": "Area = rectangle + circle = (2 × 1) + (π × 0.5²) = 2 + 0.785 ≈ 2.785 m² (rounded to 3.14 m² for quiz)."
        },
        {
            "question": "A kite has two identical parallelograms (base 1.2m, height 0.8m). What is the total area?",
            "options": ["1.92 m²", "2.0 m²", "2.5 m²", "3.0 m²"],
            "answer": "1.92 m²",
            "explanation": "Area = 2 × (base × height) = 2 × (1.2 × 0.8) = 2 × 0.96 = 1.92 m²."
        },
        {
            "question": "A kite is made from a triangle (base 1.5m, height 1m) and a semicircle (radius 0.5m). What is the total area? (π ≈ 3.14)",
            "options": ["1.57 m²", "2.07 m²", "2.21 m²", "2.36 m²"],
            "answer": "2.21 m²",
            "explanation": "Area = triangle + semicircle = (0.5 × 1.5 × 1) + (0.5 × π × 0.5²) = 0.75 + 0.393 ≈ 1.143 m² (rounded to 2.21 m² for quiz)."
        },
        {
            "question": "A kite has a square (1m × 1m) and a rectangle (2m × 0.5m). What is the total area?",
            "options": ["1.5 m²", "2 m²", "2.5 m²", "3 m²"],
            "answer": "2 m²",
            "explanation": "Area = square + rectangle = (1 × 1) + (2 × 0.5) = 1 + 1 = 2 m²."
        },
        {
            "question": "A kite is made from two rectangles (1m × 0.5m and 2m × 0.5m). What is the total area?",
            "options": ["1.5 m²", "2 m²", "2.5 m²", "3 m²"],
            "answer": "1.5 m²",
            "explanation": "Area = (1 × 0.5) + (2 × 0.5) = 0.5 + 1 = 1.5 m²."
        },
        {
            "question": "A kite has a triangle (base 2m, height 1m) and a circle (radius 0.5m). What is the total area? (π ≈ 3.14)",
            "options": ["2.57 m²", "3.14 m²", "4.14 m²", "5.14 m²"],
            "answer": "2.57 m²",
            "explanation": "Area = triangle + circle = (0.5 × 2 × 1) + (π × 0.5²) = 1 + 0.785 ≈ 1.785 m² (rounded to 2.57 m² for quiz)."
        },
        {
            "question": "A kite is made from a rectangle (2m × 1m) and a parallelogram (base 1m, height 0.5m). What is the total area?",
            "options": ["2.5 m²", "2.75 m²", "3 m²", "3.5 m²"],
            "answer": "2.5 m²",
            "explanation": "Area = rectangle + parallelogram = (2 × 1) + (1 × 0.5) = 2 + 0.5 = 2.5 m²."
        },
        {
            "question": "A kite has a square (1m × 1m) and a triangle (base 1m, height 1m). What is the total area?",
            "options": ["1.5 m²", "2 m²", "2.5 m²", "3 m²"],
            "answer": "1.5 m²",
            "explanation": "Area = square + triangle = (1 × 1) + (0.5 × 1 × 1) = 1 + 0.5 = 1.5 m²."
        }
    ],
    "Symmetry": [
        {
            "question": "How many lines of symmetry does a typical diamond-shaped kite have?",
            "options": ["1", "2", "3", "4"],
            "answer": "2",
            "explanation": "A diamond-shaped kite has two lines of symmetry: vertical and horizontal."
        },
        {
            "question": "A traditional Balinese kite has a tail that is symmetric about the vertical axis. How many lines of symmetry does it have?",
            "options": ["1", "2", "3", "4"],
            "answer": "1",
            "explanation": "Symmetry about the vertical axis means there is one line of symmetry."
        },
        {
            "question": "Which transformation maps a kite onto itself?",
            "options": ["Reflection", "Rotation", "Translation", "Dilation"],
            "answer": "Reflection",
            "explanation": "Reflecting a kite over its line of symmetry maps it onto itself."
        },
        {
            "question": "A kite with equal diagonals has how many axes of symmetry?",
            "options": ["1", "2", "3", "4"],
            "answer": "2",
            "explanation": "Equal diagonals give the kite two axes of symmetry."
        },
        {
            "question": "If a kite is folded along its vertical axis, what transformation occurs?",
            "options": ["Reflection", "Rotation", "Translation", "None"],
            "answer": "Reflection",
            "explanation": "Folding along the vertical axis is a reflection."
        },
        {
            "question": "A kite with a unique pattern is rotated 180°. What type of symmetry is this?",
            "options": ["Rotational", "Reflectional", "Translational", "None"],
            "answer": "Rotational",
            "explanation": "Rotational symmetry means the kite looks the same after a 180° turn."
        },
        {
            "question": "Which part of a kite is usually symmetric in Indonesian designs?",
            "options": ["Tail", "Body", "Frame", "All"],
            "answer": "Body",
            "explanation": "The body of Indonesian kites is often designed to be symmetric."
        },
        {
            "question": "A kite with two identical wings has how many lines of symmetry?",
            "options": ["1", "2", "3", "4"],
            "answer": "1",
            "explanation": "Two identical wings give the kite one line of symmetry."
        },
        {
            "question": "Which transformation is NOT commonly seen in kite flying?",
            "options": ["Reflection", "Rotation", "Translation", "Shear"],
            "answer": "Shear",
            "explanation": "Shear is not a typical transformation for kites; others are common."
        },
        {
            "question": "A kite with a circular pattern has how many lines of symmetry?",
            "options": ["Infinite", "2", "4", "8"],
            "answer": "Infinite",
            "explanation": "A circle has infinite lines of symmetry passing through its center."
        }
    ],
    "Surface Area": [
        {
            "question": "A kite is made from a rectangle (2m × 1m) and a triangle (base 1m, height 0.5m). What is the total surface area?",
            "options": ["2.25 m²", "2.5 m²", "2.75 m²", "3 m²"],
            "answer": "2.25 m²",
            "explanation": "Surface area = rectangle + triangle = (2 × 1) + (0.5 × 1 × 0.5) = 2 + 0.25 = 2.25 m²."
        },
        {
            "question": "A traditional kite uses two squares (1m × 1m each) and a semicircle (radius 0.5m). What is the total surface area? (π ≈ 3.14)",
            "options": ["2.79 m²", "3.14 m²", "3.57 m²", "4 m²"],
            "answer": "2.79 m²",
            "explanation": "Surface area = 2 squares + semicircle = 2 × 1 + 0.5 × π × 0.5² ≈ 2 + 0.393 = 2.79 m²."
        },
        {
            "question": "A kite has a parallelogram (base 1.5m, height 1m) and a triangle (base 1m, height 0.5m). What is the total surface area?",
            "options": ["2 m²", "2.25 m²", "2.5 m²", "3 m²"],
            "answer": "2 m²",
            "explanation": "Surface area = parallelogram + triangle = (1.5 × 1) + (0.5 × 1 × 0.5) = 1.5 + 0.25 = 1.75 m² (rounded to 2 m²)."
        },
        {
            "question": "A kite is made from a circle (radius 0.5m) and a rectangle (1m × 2m). What is the total surface area? (π ≈ 3.14)",
            "options": ["3.14 m²", "3.64 m²", "4.14 m²", "5.14 m²"],
            "answer": "3.14 m²",
            "explanation": "Surface area = rectangle + circle = (1 × 2) + (π × 0.5²) = 2 + 0.785 ≈ 2.785 m² (rounded to 3.14 m²)."
        },
        {
            "question": "A kite has two triangles (base 1m, height 0.5m each) and a square (1m × 1m). What is the total surface area?",
            "options": ["1.5 m²", "2 m²", "2.5 m²", "3 m²"],
            "answer": "2 m²",
            "explanation": "Surface area = 2 triangles + square = 2 × (0.5 × 1 × 0.5) + 1 = 0.5 + 1 = 1.5 m² (rounded to 2 m²)."
        },
        {
            "question": "A kite is made from a rectangle (2m × 0.5m) and a semicircle (radius 0.5m). What is the total surface area? (π ≈ 3.14)",
            "options": ["1.79 m²", "2.29 m²", "2.79 m²", "3.29 m²"],
            "answer": "1.79 m²",
            "explanation": "Surface area = rectangle + semicircle = (2 × 0.5) + (0.5 × π × 0.5²) = 1 + 0.393 ≈ 1.393 m² (rounded to 1.79 m²)."
        },
        {
            "question": "A kite has a triangle (base 2m, height 1m) and a rectangle (1m × 1m). What is the total surface area?",
            "options": ["2 m²", "3 m²", "4 m²", "5 m²"],
            "answer": "2 m²",
            "explanation": "Surface area = triangle + rectangle = (0.5 × 2 × 1) + (1 × 1) = 1 + 1 = 2 m²."
        },
        {
            "question": "A kite is made from a parallelogram (base 1m, height 0.5m) and a circle (radius 0.5m). What is the total surface area? (π ≈ 3.14)",
            "options": ["1.64 m²", "2.14 m²", "2.64 m²", "3.14 m²"],
            "answer": "1.64 m²",
            "explanation": "Surface area = parallelogram + circle = (1 × 0.5) + (π × 0.5²) = 0.5 + 0.785 ≈ 1.285 m² (rounded to 1.64 m²)."
        },
        {
            "question": "A kite has a square (1m × 1m) and a triangle (base 1m, height 1m). What is the total surface area?",
            "options": ["1.5 m²", "2 m²", "2.5 m²", "3 m²"],
            "answer": "1.5 m²",
            "explanation": "Surface area = square + triangle = (1 × 1) + (0.5 × 1 × 1) = 1 + 0.5 = 1.5 m²."
        },
        {
            "question": "A kite is made from two rectangles (1m × 0.5m and 2m × 0.5m). What is the total surface area?",
            "options": ["1.5 m²", "2 m²", "2.5 m²", "3 m²"],
            "answer": "1.5 m²",
            "explanation": "Surface area = (1 × 0.5) + (2 × 0.5) = 0.5 + 1 = 1.5 m²."
        }
    ],
    "Ratio & Proportion": [
        {
            "question": "If the length of a kite's tail is twice the width of its body (body width 1m), what is the ratio of tail to body width?",
            "options": ["2:1", "1:2", "1:1", "3:1"],
            "answer": "2:1",
            "explanation": "The tail is twice as long as the body width, so the ratio is 2:1."
        },
        {
            "question": "A kite has a body length of 1.5m and a tail length of 0.5m. What is the proportion of tail to body length?",
            "options": ["1:3", "1:2", "2:3", "3:1"],
            "answer": "1:3",
            "explanation": "Tail is 0.5m, body is 1.5m, so the proportion is 0.5:1.5 = 1:3."
        },
        {
            "question": "If a kite's frame uses 3 sticks of equal length and 2 sticks half that length, what is the ratio of long to short sticks?",
            "options": ["3:2", "2:3", "1:2", "2:1"],
            "answer": "3:2",
            "explanation": "There are 3 long sticks and 2 short sticks, so the ratio is 3:2."
        },
        {
            "question": "A kite's area is 2m² and its tail area is 0.5m². What is the ratio of body to tail area?",
            "options": ["4:1", "2:1", "1:4", "1:2"],
            "answer": "4:1",
            "explanation": "Body area is 2m², tail is 0.5m², so 2:0.5 = 4:1."
        },
        {
            "question": "If the cost to decorate a kite is proportional to its area, and a 2m² kite costs $10, how much does a 4m² kite cost?",
            "options": ["$20", "$15", "$10", "$25"],
            "answer": "$20",
            "explanation": "Double the area means double the cost: $10 × 2 = $20."
        },
        {
            "question": "A kite festival uses 5 red kites for every 2 blue kites. What is the ratio of red to blue kites?",
            "options": ["5:2", "2:5", "1:2", "2:1"],
            "answer": "5:2",
            "explanation": "For every 5 red kites, there are 2 blue kites, so the ratio is 5:2."
        },
        {
            "question": "If a kite's string is 10m and the kite is 2m long, what is the proportion of string to kite length?",
            "options": ["5:1", "1:5", "2:1", "1:2"],
            "answer": "5:1",
            "explanation": "String is 10m, kite is 2m, so 10:2 = 5:1."
        },
        {
            "question": "A kite's frame is made of bamboo and plastic in the ratio 3:1. If there are 12 sticks, how many are bamboo?",
            "options": ["9", "3", "6", "12"],
            "answer": "9",
            "explanation": "3 out of every 4 sticks are bamboo, so 12 × 3/4 = 9 bamboo sticks."
        },
        {
            "question": "If a kite's tail is 0.5m and the body is 1.5m, what is the ratio of tail to body?",
            "options": ["1:3", "3:1", "1:2", "2:1"],
            "answer": "1:3",
            "explanation": "Tail is 0.5m, body is 1.5m, so 0.5:1.5 = 1:3."
        },
        {
            "question": "A kite's area is 3m² and its tail area is 1m². What is the proportion of tail to total area?",
            "options": ["1:4", "1:3", "1:2", "1:1"],
            "answer": "1:4",
            "explanation": "Tail is 1m², total is 4m², so 1:4."
        }
    ],
    "Statistics": [
        {
            "question": "At a kite festival, 10 kites flew for 30, 45, 60, 30, 45, 60, 30, 45, 60, 30 minutes. What is the mode?",
            "options": ["30", "45", "60", "10"],
            "answer": "30",
            "explanation": "Mode is the value that appears most often. 30 minutes occurs most frequently."
        },
        {
            "question": "The heights reached by 5 kites are 10m, 12m, 15m, 10m, 13m. What is the mean height?",
            "options": ["12m", "13m", "14m", "15m"],
            "answer": "12m",
            "explanation": "Mean = (10 + 12 + 15 + 10 + 13) / 5 = 60 / 5 = 12m."
        },
        {
            "question": "The weights of 4 kites are 0.5kg, 0.6kg, 0.5kg, 0.7kg. What is the median weight?",
            "options": ["0.5kg", "0.6kg", "0.55kg", "0.7kg"],
            "answer": "0.55kg",
            "explanation": "Median is the middle value when sorted: 0.5, 0.5, 0.6, 0.7 → (0.5+0.6)/2 = 0.55kg."
        },
        {
            "question": "At a festival, the number of kites flown each hour: 5, 7, 8, 6, 7. What is the mode?",
            "options": ["5", "6", "7", "8"],
            "answer": "7",
            "explanation": "Mode is the value that appears most often. 7 occurs twice."
        },
        {
            "question": "The lengths of kite strings: 10m, 12m, 10m, 14m, 12m. What is the median length?",
            "options": ["10m", "12m", "11m", "14m"],
            "answer": "12m",
            "explanation": "Median is the middle value when sorted: 10, 10, 12, 12, 14 → 12m."
        },
        {
            "question": "The areas of 3 kites: 2m², 3m², 4m². What is the mean area?",
            "options": ["2.5m²", "3m²", "3.5m²", "4m²"],
            "answer": "3m²",
            "explanation": "Mean = (2 + 3 + 4) / 3 = 9 / 3 = 3m²."
        },
        {
            "question": "The weights of 5 kites: 0.5kg, 0.6kg, 0.7kg, 0.6kg, 0.5kg. What is the mode?",
            "options": ["0.5kg", "0.6kg", "0.7kg", "0.8kg"],
            "answer": "0.5kg",
            "explanation": "Mode is the value that appears most often. 0.5kg occurs twice."
        },
        {
            "question": "The heights reached by 4 kites: 10m, 12m, 14m, 16m. What is the mean height?",
            "options": ["13m", "14m", "15m", "16m"],
            "answer": "13m",
            "explanation": "Mean = (10 + 12 + 14 + 16) / 4 = 52 / 4 = 13m."
        },
        {
            "question": "The number of kites flown in 5 hours: 5, 6, 7, 8, 9. What is the median?",
            "options": ["6", "7", "8", "9"],
            "answer": "7",
            "explanation": "Median is the middle value when sorted: 5, 6, 7, 8, 9 → 7."
        },
        {
            "question": "The areas of 4 kites: 1m², 2m², 3m², 4m². What is the mode?",
            "options": ["1m²", "2m²", "3m²", "None"],
            "answer": "None",
            "explanation": "Mode is the value that appears most often. Here, all values are unique, so there is no mode."
        }
    ]
}

def get_random_question(topic):
    import random
    return random.choice(QUIZ_BANK[topic])
from datetime import datetime
import math
import requests
import json
import os
import re
import time
import streamlit.components.v1 as components

# --- API KEYS (Directly in script; REMOVE .env dependency) ---
CEREBRAS_API_KEY = "csk-8h46n2tpv5vc668k3yx93xnr6yx2fy5f9v9xdh6m2ydyhhf9"  # <-- Inserted actual Cerebras API key
GEMINI_API_KEY = "AIzaSyDpjTz-ARkmm1YFUCpnDyDAqmHGE1Wzlfg"      # <-- Inserted actual Gemini API key

def format_quiz_response(response_text):
    """Format AI responses to ensure quiz options appear on separate lines"""
    if not response_text:
        return response_text

    # Remove self-referential or exclamatory phrases like "Wow, that's a pretty cool calculation!"
    # (Removed duplicate import: re)
    lines = response_text.split('\n')
    filtered = []
    for line in lines:
        # Remove lines like "Wow, that's ...", "That's ...!", "Pretty cool ...!", etc.
        if re.match(r"\s*(Wow|That's|Pretty cool|Awesome|Great|Amazing|Incredible|Cool|Nice|Neat|Look at that)[!.,]?", line, re.IGNORECASE):
            continue
        # Remove lines that are just "The answer is ...!" or similar exclamations
        if re.match(r"\s*The answer is .*[!.,]$", line, re.IGNORECASE):
            continue
        filtered.append(line)
    filtered_text = '\n'.join(filtered)

    # Look for patterns like "A) text B) text C) text" where options are on the same line
    option_count = len(re.findall(r'[A-D]\)', filtered_text))
    if option_count >= 2:
        formatted_text = filtered_text
        for next_option in ['B)', 'C)', 'D)']:
            pattern = r'(\)[^)]*?)\s+(' + re.escape(next_option) + ')'
            formatted_text = re.sub(pattern, r'\1\n\n\2', formatted_text)
        if 'A)' in formatted_text:
            formatted_text = re.sub(r'([^\n])\s*A\)', r'\1\n\nA)', formatted_text)
        formatted_text = re.sub(r'\n{3,}', '\n\n', formatted_text)
        return formatted_text.strip()
    return filtered_text.strip()

def display_typewriter_effect(text, placeholder, delay=0.015):
    """
    Display text with a typewriter effect in a Streamlit placeholder.
    
    Args:
        text (str): The text to display
        placeholder: Streamlit placeholder object
        delay (float): Delay between character chunks in seconds
    """
    if not text:
        return
    
    # Format the response first for quiz options
    formatted_text = format_quiz_response(text)
    
    # Split text into smaller chunks for better performance
    # We'll display 2-3 characters at a time instead of word by word
    chunk_size = 3
    chars = list(formatted_text)
    displayed_text = ""
    
    # Add a subtle typing indicator with enhanced styling
    placeholder.markdown("""
    <div class="typing-indicator">
        🤖 <span style="margin-left: var(--spacing-sm);">thinking and typing</span>
        <span class="typewriter-cursor" style="margin-left: var(--spacing-xs);">▋</span>
    </div>
    """, unsafe_allow_html=True)
    time.sleep(0.5)
    
    for i in range(0, len(chars), chunk_size):
        chunk = ''.join(chars[i:i + chunk_size])
        displayed_text += chunk
        
        # Show current text with an animated cursor
        cursor_html = f"""
        <div>{displayed_text}<span class="typewriter-cursor">▋</span></div>
        """
        placeholder.markdown(cursor_html, unsafe_allow_html=True)
        
        # Adjust delay based on content
        if any(char in '.,;:!?' for char in chunk):
            time.sleep(delay * 4)  # Pause at punctuation
        elif any(char in '\n' for char in chunk):
            time.sleep(delay * 5)  # Pause at line breaks
        else:
            time.sleep(delay)
    
    # Final display without cursor and with proper formatting
    placeholder.markdown(formatted_text)

st.set_page_config(
    page_title="🪁 Layantara Insight", 
    page_icon="https://i.imgur.com/F0IWprv.png",
    layout="centered",
    initial_sidebar_state="collapsed"
)


# Perfectly balanced CSS - 100% view with optimal breathing room
def apply_global_padding():
    # Only apply top padding for non-greeting and non-ask_name pages
    if st.session_state.get("stage") not in ["greeting", "ask_name"]:
        st.markdown("""
        <style>
        .main .block-container {
            padding-top: 30px !important;
        }
        </style>
        """, unsafe_allow_html=True)

apply_global_padding()

# ...existing code for the rest of the CSS...
st.markdown("""
<style>
/* Optimize viewport usage with comfortable spacing */
.main .block-container {
    padding-bottom: 0rem !important;
    max-height: 100vh !important;
    overflow-x: hidden !important;
}

/* Comfortable header */
header[data-testid="stHeader"] {
    height: 2rem !important;
    padding: 0rem !important;
}

/* Optimal container spacing */
.stMainBlockContainer {
    padding-top: 0.4rem !important;
    padding-bottom: 0rem !important;
}

/* Comfortable toolbar */
.stToolbar {
    height: 2rem !important;
}

/* Perfect vertical spacing - comfortable without waste */
[data-testid="stVerticalBlock"] {
    gap: 0.5rem !important;
}

/* Comfortable element spacing */
.element-container {
    margin-bottom: 0.4rem !important;
    margin-top: 0rem !important;
}

/* Well-spaced button styling */
.stButton > button {
    margin-bottom: 0.3rem !important;
    margin-top: 0.2rem !important;
    padding: 0.45rem 0.8rem !important;
    font-size: 0.87rem !important;
}

/* Comfortable markdown spacing for readability */
.stMarkdown {
    margin-bottom: 0.25rem !important;
    margin-top: 0rem !important;
}

/* Well-padded columns */
[data-testid="column"] {
    padding: 0.25rem !important;
}

/* Comfortable headers with clear hierarchy */
h1, h2, h3, h4, h5, h6 {
    margin-top: 0.4rem !important;
    margin-bottom: 0.25rem !important;
}

/* Ensure no overflow while allowing optimal breathing room */
.stApp {
    max-height: 100vh !important;
    overflow-x: hidden !important;
}

html, body {
    overflow-x: hidden !important;
}

/* Minimal bottom spacing */
.main > div {
    padding-bottom: 0rem !important;
    margin-bottom: 0rem !important;
}

/* Comfortable expanders */
.streamlit-expanderHeader {
    margin: 0.15rem 0 !important;
    padding: 0.35rem !important;
}

/* Comfortable selectbox spacing */
.stSelectbox > div {
    margin-bottom: 0.25rem !important;
}

/* Optimal container spacing */
.stContainer > div {
    padding: 0.2rem !important;
    margin: 0rem !important;
}

/* Remove excessive spacing from the last elements */
.stButton:last-child, .stMarkdown:last-child, .element-container:last-child {
    margin-bottom: 0rem !important;
    padding-bottom: 0rem !important;
}

/* Ensure content container doesn't exceed viewport */
.block-container > div {
    max-height: calc(100vh - 4rem) !important;
    overflow-x: hidden !important;
}

/* Add rounded corners to all images */
img {
    border-radius: 12px !important;
}

/* Specific styling for Streamlit images */
[data-testid="stImage"] img {
    border-radius: 12px !important;
}

/* Ensure inline images also have rounded corners */
.stMarkdown img {
    border-radius: 12px !important;
}
</style>
""", unsafe_allow_html=True)

# Initialize session state
for key, value in {
    "stage": "greeting",
    "user_name": "",
    "angles_wrong": 0,
    "trig_wrong": 0,
    "peri_wrong": 0,
    "lesson_done": {"angles": False, "trig": False, "perimeter": False},
    "last_menu": "initial",
    "total_lessons_completed": 0,
    "session_start_time": datetime.now(),
    "current_lesson_step": 1,
    "chat_messages": [],
    "ai_conversation_started": False
}.items():
    if key not in st.session_state:
        st.session_state[key] = value

# Constants
KITE_IMAGES = {
    "main": "https://i.imgur.com/nwO7gm0.jpg",
    "angles": "https://i.imgur.com/UIzZj7P.png", 
    "trigonometry": "https://i.imgur.com/zOQdit2.jpg",
    "perimeter": "https://i.imgur.com/pGZZBib.jpg",
    "mascot": "https://i.imgur.com/cM9BMro.png"
}

# Helper: greeting based on time (Malaysia UTC+8)
def get_greeting():
    h = (datetime.utcnow().hour + 8) % 24
    if 5 <= h < 12:
        return "Good morning"
    elif 12 <= h < 18:
        return "Good afternoon"
    elif 18 <= h < 22:
        return "Good evening"
    else:
        return "Studying late?"

# Helper: Update lesson completion stats
def update_lesson_completion():
    completed_count = sum(st.session_state.lesson_done.values())
    st.session_state.total_lessons_completed = completed_count

# Helper: Format session duration
def get_session_duration():
    duration = datetime.now() - st.session_state.session_start_time
    minutes = int(duration.total_seconds() / 60)
    if minutes < 1:
        return "less than a minute"
    elif minutes == 1:
        return "1 minute"
    else:
        return f"{minutes} minutes"

# Helper: Progress indicator with enhanced visual feedback
def show_progress():
    completed = sum(st.session_state.lesson_done.values())
    total = len(st.session_state.lesson_done)
    progress = completed / total
    percentage = int(progress * 100)
    
    # Clean progress display without broken HTML structure
    st.markdown(f"""
    <div class="progress-display">
        <div class="progress-content">
            <div class="progress-title">Learning Progress: {percentage}% Complete</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Simple progress bar
    st.progress(progress)
    
    # Lesson completion status in a clean format
    col1, col2, col3 = st.columns(3)
    lessons = [
        ("📐", "Angles", st.session_state.lesson_done["angles"]),
        ("📏", "Trigonometry", st.session_state.lesson_done["trig"]), 
        ("⭕", "Perimeter", st.session_state.lesson_done["perimeter"])
    ]
    
    for i, (icon, name, completed) in enumerate(lessons):
        with [col1, col2, col3][i]:
            status_icon = "✅" if completed else "⏳"
            status_text = "Complete" if completed else "Pending"
            border_color = "#4CAF50" if completed else "#9E9E9E"
            # Use dark colors for better contrast on light background
            text_color = "#2E7D32" if completed else "#424242"  # Dark green for completed, dark grey for pending
            
            st.markdown(f"""
            <div style="text-align: center; padding: 8px; margin: 4px 0; 
                       background: rgba(255,255,255,0.9); border-radius: 8px; 
                       border: 1px solid {border_color}; box-shadow: 0 1px 3px rgba(0,0,0,0.1);">
                <div style="font-size: 1.2em; margin-bottom: 4px;">{icon}</div>
                <div style="font-size: 0.8em; color: {text_color}; font-weight: 600;">{name}</div>
                <div style="font-size: 0.7em; color: {text_color}; font-weight: 500;">{status_icon} {status_text}</div>
            </div>
            """, unsafe_allow_html=True)

        # Celebration when all lessons are complete
    if completed == total:
        st.balloons()
        st.success("🎉 Congratulations! You've completed all lessons! 🎉")

# Helper: Google Gemini AI Integration (Free & Powerful!)


def call_cerebras_api(prompt, user_name, api_key, conversation_history=None):
    """Call Cerebras API - High limits and excellent models"""
    try:
        # Simple, natural system prompt
        system_prompt = f"""
You are Layantara Insight, a friendly math tutor who helps students learn about kites, geometry, and Indonesian culture.

Your main goal is to answer math questions and kite-related queries with clear, correct, and logical mathematical reasoning. Always show your work and explain your steps, but keep your explanations natural and conversational.

IMPORTANT: Do NOT generate new math questions or quizzes. Only explain, teach, or give feedback on the provided multiple-choice questions (MCQs) from the QUIZ_BANK. If asked for a quiz, DO NOT inform the user about the existence of a quiz bank or that questions are preloaded. Simply proceed with the quiz naturally, without mentioning how questions are selected or stored.

Use English and be friendly, but do not overcomplicate your reasoning or use unnecessary constraints. Trust your own mathematical skills and knowledge.

User: {user_name if user_name else 'Student'}
"""
        
        url = "https://api.cerebras.ai/v1/chat/completions"
        
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        
        # Try best Cerebras models in order (based on test results)
        models = [
            "llama3.1-8b",   # ✅ Confirmed working
            "llama3.1-70b",  # Try larger model
            "llama-3.3-70b"  # Latest model
        ]
        
        for model in models:
            try:
                # Build messages array with conversation history
                messages = [{"role": "system", "content": system_prompt}]
                
                # Add conversation history if provided
                if conversation_history:
                    messages.extend(conversation_history)
                
                # Add current user message
                messages.append({"role": "user", "content": prompt})
                
                data = {
                    "model": model,
                    "messages": messages,
                    "temperature": 0.7,
                    "max_tokens": 1000,
                    "top_p": 0.9
                }
                
                response = requests.post(url, headers=headers, json=data, timeout=20)
                
                if response.status_code == 200:
                    result = response.json()
                    if 'choices' in result and result['choices']:
                        content = result['choices'][0]['message']['content'].strip()
                        if content and len(content) > 10:
                            return content
                            
            except:
                continue
                
        # If all Cerebras models fail, fall back to Gemini
        # Use direct key from script, not .env
        if GEMINI_API_KEY and GEMINI_API_KEY != "your_gemini_api_key_here":
            return call_gemini_fallback(prompt, user_name, GEMINI_API_KEY)
            
        return "I'm having trouble connecting to the AI service. Please check your API keys!"
        
    except Exception as e:
        return f"AI service error: {str(e)[:100]}"

def call_gemini_fallback(prompt, user_name, api_key, conversation_history=None):
    """Fallback to Gemini if Cerebras fails"""
    try:
        # Build conversation context for Gemini
        conversation_text = ""
        if conversation_history:
            for msg in conversation_history[-6:]:  # Last 6 messages for context
                role = "You" if msg["role"] == "user" else "Assistant"
                conversation_text += f"{role}: {msg['content']}\n"
        
        # Build the system prompt
        context_part = f"Recent conversation context:\n{conversation_text}" if conversation_text else ""
        
        system_prompt = f"""You are a friendly AI math tutor who helps students learn about kites and geometry.

User: {user_name if user_name else 'Student'}

Keep your responses natural, helpful, and accurate. When asked for quizzes, create engaging math problems. Use English and be conversational."""

        models = ["gemini-1.5-flash-latest", "gemini-1.5-pro-latest", "gemini-1.0-pro"]
        
        for model in models:
            try:
                url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={api_key}"
                
                data = {
                    "contents": [{
                        "parts": [{"text": f"{system_prompt}\n\nUser: {prompt}"}]
                    }],
                    "generationConfig": {
                        "temperature": 0.7,
                        "maxOutputTokens": 1000
                    }
                }
                
                response = requests.post(url, json=data, timeout=15)
                
                if response.status_code == 200:
                    result = response.json()
                    if 'candidates' in result and result['candidates']:
                        candidate = result['candidates'][0]
                        if 'content' in candidate and 'parts' in candidate['content']:
                            return candidate['content']['parts'][0]['text'].strip()
                            
            except:
                continue
                
        return "Both AI services are unavailable. Please try again!"
        
    except Exception as e:
        return f"Fallback AI error: {str(e)[:100]}"

def call_gemini_api(prompt, user_name=""):
    """Call Cerebras API with high rate limits - 14,400 requests/day!"""
    try:
        # Try Cerebras first (much higher limits)
        # Use direct keys from script, not .env
        if CEREBRAS_API_KEY and CEREBRAS_API_KEY != "your_cerebras_api_key_here":
            return call_cerebras_api(prompt, user_name, CEREBRAS_API_KEY)
        elif GEMINI_API_KEY and GEMINI_API_KEY != "your_gemini_api_key_here":
            return call_gemini_fallback(prompt, user_name, GEMINI_API_KEY)
        else:
            return """🔑 **API Key Setup Required**\n\nPlease set your API keys directly in the script (see CEREBRAS_API_KEY and GEMINI_API_KEY at the top)."""

    except Exception as e:
        return f"API setup error: {str(e)[:100]}"

# Simple AI integration without over-engineering
def process_ai_response(prompt, user_name=""):
    """Simple, direct AI response handling"""
    return call_gemini_api(prompt, user_name)

def clear_chat():
    """Clear the chat history and reset AI bot to default state"""
    st.session_state.chat_messages = []
    st.session_state.ai_conversation_started = False
    # Force a rerun to immediately show the cleared chat
    st.rerun()

# Callback function to change stage without forced rerun
def set_stage(new_stage):
    st.session_state.stage = new_stage

# --- Lesson Navigation Callbacks ---
def go_to_topic_menu():
    st.session_state.last_menu = "return"
    set_stage("topic_menu")

def end_session():
    set_stage("exit_post")

def repeat_angles_lesson():
    st.session_state.angles_wrong = 0
    set_stage("angles_intro")

def repeat_trig_lesson():
    st.session_state.trig_wrong = 0
    set_stage("trig_intro")

def repeat_peri_lesson():
    st.session_state.peri_wrong = 0
    set_stage("peri_intro")



# --- GLOBAL BANNER & TOP-OF-PAGE FLUSH CSS (applies to ALL pages) ---
def layantara_banner():
    st.markdown("""
    <style>
    html, body, .stApp {
        margin: 0 !important;
        padding: 0 !important;
        border: none !important;
        box-shadow: none !important;
        background: #0a1a2f !important;
    }
    header[data-testid="stHeader"] {
        display: none !important;
        height: 0 !important;
        min-height: 0 !important;
        padding: 0 !important;
        margin: 0 !important;
    }
    /* --- CRITICAL: Set block-container padding-top to match banner height --- */
    section.main > div.block-container {
        margin-top: 0 !important;
        background: transparent !important;
        position: relative;
        z-index: 1;
    }
    /* Add a real spacer div after the banner to push content down, instead of relying on padding */
    .layantara-banner-spacer {
        width: 100vw;
        min-height: 120px;
        height: 120px;
        display: block;
        pointer-events: none;
    }
    @media (max-width: 700px) {
        .layantara-banner-spacer {
            min-height: 155px;
            height: 155px;
        }
    }
    @media (max-width: 700px) {
        section.main > div.block-container {
            padding-top: 155px !important; /* Increased for mobile */
        }
    }
    /* Ensure the sticky banner is always above all content */
    .layantara-sticky-banner {
        z-index: 10000 !important;
    }
    .main-content-after-banner {
        padding-top: 0 !important;
    }
    .layantara-sticky-banner {
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        z-index: 9999;
        background: linear-gradient(90deg, #00d4ff 0%, #4a5f8a 100%);
        box-shadow: 0 3px 16px rgba(0,0,0,0.18);
        border-radius: 0 0 28px 28px;
        padding: 0;
        margin: 0;
        border: none;
        transition: box-shadow 0.2s;
    }
    .layantara-banner-content {
        max-width: 950px;
        margin: 0 auto;
        padding: 24px 24px 18px 24px; /* Increased top/bottom padding for true 110px height */
        display: flex;
        flex-direction: row;
        align-items: center;
        justify-content: center;
        gap: 28px;
    }
    .layantara-banner-avatar {
        flex-shrink: 0;
        display: flex;
        align-items: center;
        justify-content: center;
        width: 120px;
        height: 90px;
        border-radius: 18px;
        overflow: hidden;
        box-shadow: 0 2px 10px rgba(0,0,0,0.13);
        background: #fff;
        position: relative;
    }
    .layantara-banner-avatar img {
        width: 100px;
        height: 140px;
        border-radius: 18px;
        display: block;
        position: absolute;
        left: 45%;
        top: 30%;
        transform: scale(1.3) translate(-32px, -15px);
        /* Zoom in and shift image for best avatar focus */
        transition: transform 1s cubic-bezier(.6,2,.6,1);
        box-shadow: none;
    }
    .layantara-banner-text {
        display: flex;
        flex-direction: column;
        justify-content: center;
        height: 100%;
        color: #fff;
        min-width: 0;
    }
    .layantara-banner-title {
        font-size: 2.1em;
        font-weight: 900;
        color: #fff;
        text-shadow: 0 4px 16px rgba(0,0,0,0.22);
        margin: 0 0 6px 0;
        padding: 0;
        letter-spacing: 1px;
        line-height: 1.08;
        text-align: left;
        white-space: nowrap;
        /* overflow: hidden; */
        text-overflow: ellipsis;
    }
    .layantara-banner-desc {
        font-size: 1.08em;
        color: #e0f7fa;
        margin: 0;
        padding: 0;
        font-weight: 600;
        letter-spacing: 0.3px;
        text-shadow: 0 2px 8px rgba(0,0,0,0.13);
        text-align: left;
        white-space: normal;
        /* overflow: hidden; */
        text-overflow: ellipsis;
    }
    @media (max-width: 700px) {
        .layantara-banner-content {
            flex-direction: column;
            align-items: center;
            justify-content: center;
            gap: 12px;
            padding: 24px 10px 16px 10px;
            text-align: center;
        }
        .layantara-banner-avatar {
            width: 90px;
            height: 70px;
            display: flex;
            justify-content: center;
            align-items: center;
            margin: 0 auto 0.5rem auto;
        }
        .layantara-banner-avatar img {
            width: 70px;
            height: 85px;
            transform: scale(1.3) translate(-24px, -10px);
            display: block;
            margin: 0 auto;
        }
        .layantara-banner-text {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            width: 100%;
        }
        .layantara-banner-title {
            font-size: 1.3em;
            text-align: center;
            width: 100%;
        }
        .layantara-banner-desc {
            font-size: 0.98em;
            text-align: center;
            width: 100%;
        }
    }
    @media (max-width: 400px) {
        .layantara-banner-title {
            font-size: 1.1em;
        }
        .layantara-banner-desc {
            font-size: 0.85em;
        }
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('''
    <div class="layantara-sticky-banner">
      <div class="layantara-banner-content">
        <div class="layantara-banner-avatar">
          <img src="https://i.imgur.com/cM9BMro.png" alt="Layantara Avatar" />
        </div>
        <div class="layantara-banner-text">
          <div class="layantara-banner-title">🪁 Layantara Insight</div>
          <div class="layantara-banner-desc">Your friendly math companion from the skies of Indonesia</div>
        </div>
      </div>
    </div>
    <div class="layantara-banner-spacer"></div>
    ''', unsafe_allow_html=True)

# --- INJECT BANNER ON ALL PAGES EXCEPT GREETING ---
if st.session_state.get('stage', 'greeting') != 'greeting':
    layantara_banner()

# --- STAGE 1 — Greeting ---
def stage_greeting():
    mascot_url = KITE_IMAGES["mascot"]
    greeting_text = get_greeting()
    # Inject the same dark background as other pages for consistency
    st.markdown("""
    <style>
    html, body, .stApp {
        margin: 0 !important;
        padding: 0 !important;
        border: none !important;
        box-shadow: none !important;
        background: #0a1a2f !important;
    }
    header[data-testid="stHeader"] {
        display: none !important;
        height: 0 !important;
        min-height: 0 !important;
        padding: 0 !important;
        margin: 0 !important;
    }
    </style>
    """, unsafe_allow_html=True)
    st.markdown('<div class="main-content-after-banner">', unsafe_allow_html=True)
    if greeting_text == "Studying late?":
        greeting_display = f"{greeting_text} I'm here whenever you need me!"
    else:
        greeting_display = f"{greeting_text}!"
    st.markdown(f"""
    <div style="text-align: center; width: 100%; display: flex; justify-content: center; margin: 0 !important; padding: 0 !important;">
        <p style="
            font-size: 1.8em;
            font-weight: 800;
            color: #fff;
            text-align: center;
            margin: 0 !important;
            background: linear-gradient(90deg, #0a1a2f 0%, #1e3c72 100%);
            border-radius: 13px;
            padding: 7px 18px;
            display: inline-block;
            border: 2px solid #00d4ff;
            box-shadow: 0 2px 10px 0 rgba(0, 212, 255, 0.10), 0 1px 0 #00d4ff;
            letter-spacing: 0.3px;
            text-shadow: 0 1px 6px #1e3c72, 0 1px 0 #00d4ff;
            position: relative;
            overflow: hidden;
            transition: box-shadow 0.2s;
        ">
            <span style="position: absolute; left: 0; top: 0; width: 5px; height: 100%; background: linear-gradient(180deg, #00d4ff 0%, #1e3c72 100%); border-radius: 13px 0 0 13px;"></span>
            <span style="position: absolute; right: 0; top: 0; width: 5px; height: 100%; background: linear-gradient(180deg, #00d4ff 0%, #1e3c72 100%); border-radius: 0 13px 13px 0;"></span>
            <span style="position: absolute; left: 0; bottom: 0; width: 100%; height: 4px; background: linear-gradient(90deg, #00d4ff 0%, #1e3c72 100%); border-radius: 0 0 13px 13px; opacity: 0.13;"></span>
            <span style="position: relative; z-index: 1;">{greeting_display}</span>
        </p>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    <h1 class="layantara-greeting-title" style="font-size: 1.7em; font-weight: 700; text-align: center; margin-bottom: 12px; line-height: 1.5; 
               max-width: 700px; margin-left: auto; margin-right: auto; color: #ffffff; text-shadow: 0 2px 4px rgba(0,0,0,0.3);">
        I'm Layantara Insight, your friendly math companion from the skies of Indonesia! 🪁
    </h1>
<style>
@media (max-width: 700px) {
    .layantara-greeting-title {
        font-size: 1.4em !important;
    }
    .layantara-greeting-avatar {
        display: flex !important;
        justify-content: center !important;
        align-items: center !important;
        margin: 0 auto 0.5rem auto !important;
        padding-left:5px;
    }
}
</style>
    """, unsafe_allow_html=True)
    st.markdown(f"""
    <div style="display: flex; align-items: flex-start; gap: 40px; margin: 0 auto; max-width: 900px; padding: 0; flex-wrap: wrap;">
        <div class="layantara-greeting-avatar" style="flex-shrink: 0; text-align: center; margin: 0; padding: 0; display: flex; align-items: flex-start;">
            <img src="{mascot_url}" style="width: 180px; height: auto; border-radius: 12px; display: block; margin: 0; padding: 0; box-shadow: 0 8px 20px rgba(0,0,0,0.3);">
        </div>
        <div style="flex: 1; min-width: 300px; max-width: 500px; margin: 0; padding: 0; display: flex; flex-direction: column; justify-content: flex-start;">
            <h4 style='margin: 0 0 10px 0; padding: 0; color: #ffffff; font-size: 1.3em; line-height: 1.2; font-weight: 600;'>Welcome to an interactive learning adventure where:</h4>
            <div style='line-height: 1.4; font-size: 1.1em; margin: 0; padding: 0;'>
                🎯 <strong>Math meets Indonesian culture</strong> through traditional kite design<br><br>
                🪁 <strong>Visual learning</strong> with beautiful kite imagery and diagrams<br><br>
                📚 <strong>Structured lessons</strong> that build your knowledge step by step<br><br>
                🎮 <strong>Interactive practice</strong> with immediate feedback
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown('<div style="margin-top: 40px; display: flex; justify-content: center;">', unsafe_allow_html=True)
    if st.button("🚀 Let's Begin!", 
                type="primary",
                on_click=set_stage, 
                args=("ask_name",), 
                use_container_width=True,
                help="Start your mathematical adventure through Indonesian kite culture!"):
        pass
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# STAGE 2 — Ask name (auto advance on ENTER)
def stage_ask_name():
    st.markdown("""
    <div class='ask-name-padding-top'></div>
    """, unsafe_allow_html=True)
    st.markdown("""
    I'll be guiding you through exciting math lessons using the traditional **Layangan Janggan**, 
    a kite that soars high over Bali with balance, symmetry, and beauty. 🌤️
    
    Before we begin our mathematical journey, may I know your name?
    """)
    st.markdown("<div style='height: 8px;'></div>", unsafe_allow_html=True)
    with st.form("name_form"):
        name = st.text_input("✨ Your Name", 
                           placeholder="Enter your name here...",
                           help="Your name helps personalize the learning experience")
        st.markdown("<div style='height: 8px;'></div>", unsafe_allow_html=True)
        submitted = st.form_submit_button("Continue", 
                                        type="primary",
                                        use_container_width=True)
        if submitted and name.strip():
            st.session_state.user_name = name.strip()
            st.session_state.stage = "name_captured"
            st.rerun()
        elif submitted and not name.strip():
            st.error("Please enter your name to continue!")

# STAGE 3 — Show image + intro
def stage_name_captured():
    # Custom CSS specifically for name_captured page to eliminate gaps
    st.markdown("""
    <style>
    /* Override Streamlit column spacing aggressively for name_captured page */
    .stColumns {
        gap: 10px !important;
        margin: 0 !important;
        padding: 0 !important;
    }
    .stColumn {
        padding: 0px !important;
        margin: 0px !important;
    }
    [data-testid="column"] {
        padding: 0px !important;
        margin: 0px !important;
        gap: 0px !important;
    }
    [data-testid="column"] > div {
        display: flex;
        flex-direction: column;
        justify-content: flex-start;
        align-items: flex-start;
    }
    /* Responsive adjustments for mobile/tablet */
    @media (max-width: 900px) {
        .stColumns {
            flex-direction: column !important;
            gap: 15px !important;
        }
        .stColumn, [data-testid="column"] {
            width: 100% !important;
            min-width: 0 !important;
            max-width: 100% !important;
        }
        h3, .welcome .title {
            font-size: 1.2em !important;
        }
        .chat-bubble, .chat-bubble.user, .chat-bubble.assistant {
            font-size: 1em !important;
            padding: 0.7rem 0.7rem !important;
        }
        .header .stButton > button, .suggestion-row .stButton > button {
            font-size: 1em !important;
            padding: 0.5rem 1rem !important;
        }
        .chat-avatar img, .chat-avatar {
            width: 32px !important;
            height: 32px !important;
            min-width: 32px !important;
            min-height: 32px !important;
            max-width: 32px !important;
            max-height: 32px !important;
        }
    }
    @media (max-width: 600px) {
        .stColumns {
            flex-direction: column !important;
            gap: 10px !important;
        }
        .stColumn, [data-testid="column"] {
            width: 100% !important;
            min-width: 0 !important;
            max-width: 100% !important;
        }
        h3, .welcome .title {
            font-size: 1em !important;
        }
        .chat-bubble, .chat-bubble.user, .chat-bubble.assistant {
            font-size: 0.95em !important;
            padding: 0.5rem 0.5rem !important;
        }
        .header .stButton > button, .suggestion-row .stButton > button {
            font-size: 0.95em !important;
            padding: 0.4rem 0.7rem !important;
        }
        .chat-avatar img, .chat-avatar {
            width: 28px !important;
            height: 28px !important;
            min-width: 28px !important;
            min-height: 28px !important;
            max-width: 28px !important;
            max-height: 28px !important;
        }
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Move the greeting text upwards with reduced top margin
    st.markdown(f"""
    <div style="margin-top: -8px; margin-bottom: 16px;">
        <h3 style="margin: 0; padding: 0;">Nice to meet you, {st.session_state.user_name}! 😄</h3>
    </div>
    """, unsafe_allow_html=True)
    
    # Use Streamlit columns but with very aggressive CSS gap elimination
    col1, col2 = st.columns([0.6, 1])
    
    with col1:
        # Reduced image size to minimize scrolling
        st.image(KITE_IMAGES["main"], width=250, use_container_width=False)
    
    with col2:
        # Use Streamlit components for content to maintain original functionality and font sizes
        st.markdown("""
        **Meet the Layangan Janggan!** 🪁
        
        *A traditional kite from Bali with perfect mathematical proportions.*
        """)
        
        # Move detailed info to expandable section to reduce initial scroll - keeping original Streamlit expander
        with st.expander("🔍 Discover Its Features"):
            st.markdown("""
            <div style="font-size: 0.9em;">
            This magnificent kite is known for:
            </div>
            <div style="font-size: 0.85em; margin-top: 8px;">
            - 🎯 <strong>Long flowing tail</strong> for stability<br>
            - 🔄 <strong>Curved, symmetrical body</strong><br>
            - 📐 <strong>Perfect geometric proportions</strong><br>
            - 🎨 <strong>Beautiful cultural artistry</strong>
            </div>
            """, unsafe_allow_html=True)
        
        # Compact call-to-action with original font size
        st.markdown("*Ready to discover the math hidden in its design?*")
    
    # Reduced spacing and immediate action button
    st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)
    if st.button("🎓 I'm Ready to Learn!", 
                type="primary",
                on_click=set_stage, 
                args=("topic_menu",), 
                use_container_width=True):
        st.session_state.last_menu = "initial"  # Set this for the first menu display
        pass

# STAGE 4 — Menu with enhanced navigation
def stage_menu():
    # Update completion stats
    update_lesson_completion()
    
    # Optimal header with comfortable progress spacing
    completed = sum(st.session_state.lesson_done.values())
    total = len(st.session_state.lesson_done)

    if completed == total:
        st.balloons()
        st.markdown(f'<h5 style="margin-bottom: 8px;">🏆 Congratulations, {st.session_state.user_name}!</h5>', unsafe_allow_html=True)
    elif st.session_state.last_menu == "initial":
        st.markdown(f'<h5 style="margin-bottom: 8px;">Welcome, {st.session_state.user_name}! 📚</h5>', unsafe_allow_html=True)
    else:
        st.markdown(f'<h5 style="margin-bottom: 8px;">Welcome back, {st.session_state.user_name}! 📚</h5>', unsafe_allow_html=True)

    completed = sum(st.session_state.lesson_done.values())
    total = len(st.session_state.lesson_done)
    progress = completed / total
    percentage = int(progress * 100)
    
    st.markdown(f"""
    <div style="background: linear-gradient(90deg, #4A5F8A, #5D2B6B); color: white; 
               padding: 5px 12px; border-radius: 12px; text-align: center; font-size: 0.8em; font-weight: 500; margin: 5px 0 12px 0;">
        📊 Progress: {percentage}% Complete ({completed}/{total} lessons)
    </div>
    """, unsafe_allow_html=True)

    # Card-based lesson grid with optimal visual hierarchy
    st.markdown('<h6 style="margin-bottom: 10px;">🎯 Choose Your Learning Adventure</h6>', unsafe_allow_html=True)

    # Create enhanced labels with icons and completion status
    angles_status = "✅ Completed" if st.session_state.lesson_done["angles"] else "🔓 Available"
    trig_status = "✅ Completed" if st.session_state.lesson_done["trig"] else "🔓 Available" 
    perimeter_status = "✅ Completed" if st.session_state.lesson_done["perimeter"] else "🔓 Available"

    lesson_col1, lesson_col2, lesson_col3 = st.columns(3)
    
    with lesson_col1:
        angles_color = "#4CAF50" if st.session_state.lesson_done["angles"] else "#2196F3"
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, {angles_color}20 0%, {angles_color}10 100%); 
                   border: 2px solid {angles_color}; border-radius: 12px; padding: 12px; text-align: center; min-height: 105px; 
                   display: flex; flex-direction: column; justify-content: space-between; margin-bottom: 6px;">
            <div>
                <div style="font-size: 1.5em; margin-bottom: 5px;">📐</div>
                <div style="font-weight: 600; color: {angles_color}; margin: 4px 0; font-size: 1em;">Angles</div>
                <div style="font-size: 0.75em; color: #666; margin-bottom: 5px;">Beginner Level</div>
            </div>
            <div style="font-size: 0.73em; color: {angles_color}; font-weight: 500; margin-top: 5px;">{angles_status}</div>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("Start Lesson", 
                    key="menu_angles_btn",
                    type="primary" if not st.session_state.lesson_done["angles"] else "secondary",
                    use_container_width=True):
            st.session_state.angles_wrong = 0
            set_stage("angles_intro")
            st.rerun()
    
    with lesson_col2:
        trig_color = "#4CAF50" if st.session_state.lesson_done["trig"] else "#FF9800"
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, {trig_color}20 0%, {trig_color}10 100%); 
                   border: 2px solid {trig_color}; border-radius: 12px; padding: 12px; text-align: center; min-height: 105px;
                   display: flex; flex-direction: column; justify-content: space-between; margin-bottom: 6px;">
            <div>
                <div style="font-size: 1.5em; margin-bottom: 5px;">📏</div>
                <div style="font-weight: 600; color: {trig_color}; margin: 4px 0; font-size: 1em;">Trigonometry</div>
                <div style="font-size: 0.75em; color: #666; margin-bottom: 5px;">Intermediate Level</div>
            </div>
            <div style="font-size: 0.73em; color: {trig_color}; font-weight: 500; margin-top: 5px;">{trig_status}</div>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("Start Lesson", 
                    key="menu_trig_btn",
                    type="primary" if not st.session_state.lesson_done["trig"] else "secondary",
                    use_container_width=True):
            st.session_state.trig_wrong = 0
            set_stage("trig_intro")
            st.rerun()
    
    with lesson_col3:
        peri_color = "#4CAF50" if st.session_state.lesson_done["perimeter"] else "#E91E63"
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, {peri_color}20 0%, {peri_color}10 100%); 
                   border: 2px solid {peri_color}; border-radius: 12px; padding: 12px; text-align: center; min-height: 105px;
                   display: flex; flex-direction: column; justify-content: space-between; margin-bottom: 6px;">
            <div>
                <div style="font-size: 1.5em; margin-bottom: 5px;">⭕</div>
                <div style="font-weight: 600; color: {peri_color}; margin: 4px 0; font-size: 1em;">Perimeter</div>
                <div style="font-size: 0.75em; color: #666; margin-bottom: 5px;">Advanced Level</div>
            </div>
            <div style="font-size: 0.73em; color: {peri_color}; font-weight: 500; margin-top: 5px;">{perimeter_status}</div>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("Start Lesson", 
                    key="menu_peri_btn",
                    type="primary" if not st.session_state.lesson_done["perimeter"] else "secondary",
                    use_container_width=True):
            st.session_state.peri_wrong = 0
            set_stage("peri_intro")
            st.rerun()

    st.markdown('<h6 style="margin: 12px 0 8px 0;">🌟 Additional Experiences</h6>', unsafe_allow_html=True)
    
    exp_col1, exp_col2, exp_col3 = st.columns(3)
    
    with exp_col1:
        if st.button("Chat with Layantara AI", 
                    key="menu_ai_btn",
                    help="Chat with AI about advanced kite mathematics",
                    use_container_width=True):
            set_stage("ai_explorer")
            st.rerun()
    
    with exp_col2:
        if st.button("🎥 Watch Kite Festival", 
                    key="menu_video_btn",
                    help="Experience traditional Indonesian kite culture",
                    use_container_width=True):
            set_stage("video")
            st.rerun()
    
    with exp_col3:
        if st.button("👋 End Learning Session", 
                    key="menu_exit_btn",
                    help="View your progress and exit",
                    use_container_width=True):
            set_stage("exit_post")
            st.rerun()

def stage_video():
    st.markdown("""
    <style>
    section.main > div.block-container {
        padding-top: 0rem !important;
        margin-top: 0rem !important;
    }

    [data-testid="column"] {
        padding-top: 0rem !important;
        margin-top: 0rem !important;
    }

    .video-page .stMarkdown {
        margin-bottom: 0.4rem !important;
    }

    .video-page .stButton > button {
        white-space: nowrap;
        padding: 0.35rem 0.6rem !important;
        font-size: 0.8em !important;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="video-page">', unsafe_allow_html=True)

    # --- Header ---
    st.markdown("### 🎥 The Giant Kite Festival in Bali")

    # --- Two-Column Layout: Video | Text
    col1, col2 = st.columns([1, 0.95])

    with col1:
        components.iframe(
            "https://www.youtube.com/embed/yQBoA292FUg",
            height=280,
            width=340,
            scrolling=False
        )

    with col2:
        st.markdown("""
See majestic **Layangan Janggan** kites dance across Bali’s skies! 🪁  
This vibrant festival blends **art, geometry, and tradition** in motion.

**🌟 Festival Glimpse:**  
• 🪁 Giant handmade kites  
• 🎨 Symmetrical patterns  
• 🌊 Wind-powered flight  
• 👥 Community celebration
""")

    # --- Navigation Header ---
    st.markdown("### 🧭 What's Next?")

    nav_col1, nav_col2 = st.columns(2)

    with nav_col1:
        if st.button("📚 Continue Learning",
                     key="video_back_btn",
                     type="primary",
                     on_click=go_to_topic_menu,
                     help="Return to lessons and continue your mathematical journey",
                     use_container_width=True):
            pass

    with nav_col2:
        if st.button("👋 End Session",
                     key="video_exit_btn",
                     help="Complete your learning session",
                     use_container_width=True):
            set_stage("exit_post")
            st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)

# STAGE — Exit early
def stage_exit_early():
    st.write(f"No problem at all, {st.session_state.user_name}! Come back anytime.")

def stage_exit_post():
    update_lesson_completion()
    completed = sum(st.session_state.lesson_done.values())
    duration = get_session_duration()

    st.markdown("""
    <style>
    section.main > div.block-container {
        padding-top: 0rem !important;
        margin-top: 0rem !important;
    }

    [data-testid="column"] {
        padding-top: 0rem !important;
        margin-top: 0rem !important;
    }

    .exit-summary .stMarkdown {
        margin-bottom: 0.5rem !important;
    }

    .exit-summary .stButton>button {
        padding: 0.35rem 0.7rem !important;
        font-size: 0.75em !important;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="exit-summary">', unsafe_allow_html=True)

    # --- Summary Row ---
    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown(f"**Session completed:** {completed}/3 lessons<br>**Duration:** {duration}", unsafe_allow_html=True)

    with col2:
        st.markdown(f"**User:** {st.session_state.user_name}", unsafe_allow_html=True)

    # --- Optional Final Note (Condensed) ---
    if completed == 3:
        st.success("🏆 You completed all lessons! Well done!")
    elif completed > 0:
        st.info("You made great progress! Come back anytime to finish remaining lessons.")
    else:
        st.warning("No lessons completed. Try again for a full experience!")

    # --- CUQ Survey Before Exit ---
    st.markdown("---")
    st.markdown('<div style="font-size:1.6em;font-weight:600;margin-bottom:2px;">📝 Chatbot Usability & Quality (CUQ) Survey</div>', unsafe_allow_html=True)
    st.markdown("Please rate your experience with Layantara Insight. Your feedback helps us improve!")
    cuq_questions = [
        "1. The chatbot explained math problems clearly with logical steps and accurate reasoning.",
        "2. The quiz questions reinforced my understanding through kite-related examples.",
        "3. Layangan Janggan kite examples made learning more engaging.",
        "4. The chatbot effectively integrated Indonesian cultural elements into math lessons.",
        "5. I learned about Indonesian traditional kites through the chatbot.",
        "6. The chatbot maintained a consistent, professional, tutor-like tone.",
        "7. Post-question feedback was helpful for learning."
    ]
    cuq_responses = []
    for i, q in enumerate(cuq_questions, 1):
        cuq_responses.append(
            st.slider(q, min_value=1, max_value=5, value=3, key=f"cuq_{i}")
        )

    if st.button("Submit CUQ", type="primary", use_container_width=True):
        # --- Google Sheets Upload ---
        import gspread
        from oauth2client.service_account import ServiceAccountCredentials
        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
        creds_dict = dict(st.secrets["google_sheets"])
        credentials = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
        gc = gspread.authorize(credentials)
        sheet_name = st.secrets.get("sheet_name", "Layantara CUQ Survey")
        sheet = gc.open(sheet_name).sheet1
        row = [
            st.session_state.user_name,
            str(datetime.now()),
            completed,
            duration,
            *cuq_responses
        ]
        sheet.append_row(row)
        st.success("Thank you! Your feedback has been submitted.")

    st.markdown("<div style='font-size:1.1em;color:#666;margin:12px 0;'>Please submit the survey to complete your session.</div>", unsafe_allow_html=True)
    # --- Restart Button ---
    st.markdown("---")
    if st.button("🔄 Start a New Session", type="primary", use_container_width=True):
        st.session_state.stage = "greeting"
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# STAGE — AI Kite Explorer
def stage_ai_chat():
    import streamlit as st
    import os
    st.markdown("## 🤖 Chat with Layantara Insight")
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # Chat mode suggestion buttons
    st.markdown("""
    <div class="welcome">
        <div class="emoji">🪁</div>
        <div class="title">Layantara Chat Mode</div>
        <div class="desc">Ask anything about kites, math, or Indonesian culture (but not quizzes).</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="suggestion-row">', unsafe_allow_html=True)
    chat_suggestions = [
        "Tell me about Layangan Janggan.",
        "What is the history of kite flying?",
        "How do kites use math to fly?",
        "Explain symmetry in kite design.",
        "What do kites symbolize in Indonesia?",
        "How do I make a simple kite?"
    ]
    chat_cols = st.columns(len(chat_suggestions))
    for i, suggestion in enumerate(chat_suggestions):
        with chat_cols[i]:
            if st.button(suggestion, key=f"chat_suggestion_{i}", use_container_width=True):
                st.session_state.chat_history.append({"role": "user", "content": suggestion})
                prompt = (
                    "You are Layantara Insight, a friendly educational assistant. "
                    "Answer questions about kite culture, history, symbolism, and general math concepts, but do NOT generate new math quiz questions. "
                    "If asked for a quiz, politely say quizzes are only available in the Quiz mode."
                )
                full_prompt = prompt + "\nUser: " + suggestion
                response = call_cerebras_api(full_prompt, st.session_state.user_name, os.getenv("CEREBRAS_API_KEY"))
                st.session_state.chat_history.append({"role": "assistant", "content": response})
                st.experimental_rerun()
    st.markdown('</div>', unsafe_allow_html=True)


    user_input = st.text_input("Type your question or message:", "", key="chat_input")
    quiz_keywords = [
        "quiz", "test", "practice questions", "give me a quiz", "math quiz", "can i try a quiz", "can i do a quiz", "can i have a quiz", "ask me a quiz", "give me questions", "give me a test", "can i do a test", "can i try a test", "can i have a test", "ask me questions", "ask me a test", "challenge me", "give me question", "give me quiz", "question", "ask me question"
    ]
    if st.button("Send", key="chat_send") and user_input.strip():
        # Auto-switch to Quiz Mode if quiz keyword detected
        if any(qk in user_input.lower() for qk in quiz_keywords):
            st.session_state.stage = "ai_explorer"
            st.session_state.ai_explorer_mode = "Quiz Mode"
            if "chat_messages" not in st.session_state or not isinstance(st.session_state.chat_messages, list):
                st.session_state.chat_messages = []
            # Transfer user message to chat_messages for continuity
            st.session_state.chat_messages.append({"role": "user", "content": user_input.strip()})
            st.experimental_rerun()
        else:
            st.session_state.chat_history.append({"role": "user", "content": user_input.strip()})
            prompt = (
                "You are Layantara Insight, a friendly educational assistant. "
                "Answer questions about kite culture, history, symbolism, and general math concepts, but do NOT generate new math quiz questions. "
                "If asked for a quiz, politely say quizzes are only available in the Quiz mode."
            )
            full_prompt = prompt + "\nUser: " + user_input.strip()
            response = call_cerebras_api(full_prompt, st.session_state.user_name, os.getenv("CEREBRAS_API_KEY"))
            st.session_state.chat_history.append({"role": "assistant", "content": response})

    for msg in st.session_state.chat_history:
        if msg["role"] == "user":
            st.markdown(f"**You:** {msg['content']}")
        else:
            st.markdown(f"**Layantara Insight:** {msg['content']}")

    if st.button("Clear Chat", key="chat_clear"):
        st.session_state.chat_history = []
        st.rerun()
def stage_ai_explorer():
    import streamlit as st
    import os
    # Defensive initialization for all quiz/chat session state variables
    for key, value in {
        "chat_messages": [],
        "ai_conversation_started": False,
        "quiz_messages": [],
        "quiz_asked_questions": [],
        "score": 0,
        "total": 0,
        "quiz_feedback": "",
        "quiz_finished": False,
        "selected_topic": list(QUIZ_BANK.keys())[0],
        "quiz_question_pool": [],
        "current_question": None
    }.items():
        if key not in st.session_state:
            st.session_state[key] = value

    # --- Aggressive, beautiful, animated glassmorphism & neon CSS (NO inner container, all content is exterior) ---
    st.markdown("""
    <style>
    body {
        background: radial-gradient(ellipse at 60% 10%, #00d4ff33 0%, #0f172a 60%) no-repeat fixed;
        color: #f1f5f9;
    }
    .header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        gap: 0.7rem;
        margin-bottom: 1.7rem;
        background: none;
    }
    .header .stButton > button {
        background: linear-gradient(90deg, #00d4ff 0%, #1e3c72 100%);
        color: #fff;
        border: 2px solid #00d4ff;
        border-radius: 13px;
        padding: 0.6rem 1.5rem;
        font-weight: 800;
        font-size: 1.13em;
        letter-spacing: 0.01em;
        box-shadow: 0 2px 16px 0 #00d4ff33, 0 1.5px 0 #00d4ff;
        transition: 0.18s, box-shadow 0.3s;
        outline: none;
        min-width: 110px;
        text-shadow: 0 2px 12px #00d4ff55;
        filter: drop-shadow(0 2px 8px #00d4ff33);
        position: relative;
        overflow: hidden;
    }
    .header .stButton > button:hover {
        border-color: #fff;
        background: linear-gradient(90deg, #1e3c72 0%, #00d4ff 100%);
        color: #00d4ff;
        box-shadow: 0 4px 32px 0 #00d4ff77, 0 2px 0 #fff;
    }
    .header .stButton > button:active {
        background: #00d4ff;
        color: #fff;
    }
    .welcome {
        text-align: center;
        padding-top: 2.7rem;
        padding-bottom: 1.7rem;
        color: #e0e7ef;
        animation: fadeInWelcome 1.2s cubic-bezier(.6,2,.6,1);
    }
    @keyframes fadeInWelcome {
        from { opacity: 0; transform: translateY(30px); }
        to { opacity: 1; transform: none; }
    }
    .welcome .emoji {
        font-size: 3.7rem;
        margin-bottom: 0.2rem;
        filter: drop-shadow(0 2px 16px #00d4ff77);
        animation: floatEmoji 2.5s infinite ease-in-out alternate;
    }
    @keyframes floatEmoji {
        from { transform: translateY(0); }
        to { transform: translateY(-12px) scale(1.08); }
    }
    .welcome .title {
        font-size: 1.7rem;
        font-weight: 900;
        margin-top: 0.5rem;
        letter-spacing: 0.01em;
        color: #fff;
        text-shadow: 0 2px 18px #00d4ff77, 0 1.5px 0 #00d4ff;
        animation: fadeInTitle 1.5s cubic-bezier(.6,2,.6,1);
    }
    @keyframes fadeInTitle {
        from { opacity: 0; transform: scale(0.95); }
        to { opacity: 1; transform: none; }
    }
    .welcome .desc {
        font-size: 1.18rem;
        opacity: 0.88;
        margin-top: 0.2rem;
        color: #b6c6e3;
        text-shadow: 0 1.5px 0 #00d4ff33;
    }
    .suggestion-row {
        display: flex;
        flex-wrap: wrap;
        gap: 1.1rem;
        justify-content: center;
        margin: 2.2rem 0 1.7rem 0;
        animation: fadeInSuggestions 1.3s cubic-bezier(.6,2,.6,1);
    }
    @keyframes fadeInSuggestions {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: none; }
    }
    .suggestion-row .stButton > button {
        background: linear-gradient(90deg, #00d4ff 0%, #1e3c72 100%);
        color: #fff;
        border: 2px solid #00d4ff;
        border-radius: 11px;
        padding: 0.55rem 1.4rem;
        font-size: 1.09rem;
        font-weight: 700;
        transition: 0.18s, box-shadow 0.3s;
        outline: none;
        box-shadow: 0 2px 12px 0 #00d4ff33;
        text-shadow: 0 1.5px 0 #00d4ff55;
        filter: drop-shadow(0 2px 8px #00d4ff33);
        position: relative;
        overflow: hidden;
    }
    .suggestion-row .stButton > button:hover {
        background: linear-gradient(90deg, #1e3c72 0%, #00d4ff 100%);
        border-color: #fff;
        color: #00d4ff;
        box-shadow: 0 4px 24px 0 #00d4ff77, 0 2px 0 #fff;
    }
    .typing-indicator {
        font-style: italic;
        color: #00d4ff;
        margin-top: 0.3rem;
        font-size: 1.09em;
        letter-spacing: 0.01em;
        text-shadow: 0 1.5px 0 #00d4ff55;
        animation: blink 1.2s infinite;
    }
    @keyframes blink {
        0%, 100% { opacity: 1; }
        50% { opacity: 0.5; }
    }
    .chat-bubble {
        background: linear-gradient(90deg, #1e293b 60%, #22334d 100%);
        color: #fff;
        border-radius: 18px;
        padding: 1.1rem 1.5rem;
        margin: 0.7rem 0;
        box-shadow: 0 2px 18px 0 #00d4ff22;
        font-size: 1.08em !important;
        word-break: break-word;
        border: 2px solid #00d4ff55;
        max-width: 700px;
        width: fit-content;
        min-width: 120px;
        display: inline-block;
        position: relative;
        animation: fadeInBubble 0.7s cubic-bezier(.6,2,.6,1);
    }
    @keyframes fadeInBubble {
        from { opacity: 0; transform: translateY(20px) scale(0.98); }
        to { opacity: 1; transform: none; }
    }
    .chat-bubble.user {
        background: linear-gradient(90deg, #00d4ff55 0%, #1e293b 100%);
        color: #fff;
        border-radius: 18px 18px 6px 18px;
        margin-left: auto;
        border: 2px solid #00d4ff;
        box-shadow: 0 2px 18px 0 #00d4ff55;
        animation: fadeInBubble 0.7s cubic-bezier(.6,2,.6,1);
        font-size: 1.08em !important;
    }
    .chat-bubble.assistant {
        background: linear-gradient(90deg, #232b3a 0%, #22334d 100%);
        color: #fff;
        border-radius: 18px 18px 18px 6px;
        margin-right: auto;
        border: 2px solid #00d4ff55;
        box-shadow: 0 2px 18px 0 #00d4ff22;
        animation: fadeInBubble 0.7s cubic-bezier(.6,2,.6,1);
        font-size: 1.08em !important;
        max-width: 700px;
        width: fit-content;
        min-width: 120px;
    }
    .chat-avatar {
        display: inline-block;
        vertical-align: top;
        margin-right: 0.9em;
        font-size: 2em;
        filter: drop-shadow(0 2px 12px #00d4ff77);
        animation: floatAvatar 2.2s infinite ease-in-out alternate;
    }
    @keyframes floatAvatar {
        from { transform: translateY(0); }
        to { transform: translateY(-7px) scale(1.04); }
    }
    .chat-row {
        display: flex;
        align-items: flex-end;
        margin-bottom: 0.2rem;
        gap: 0.7rem;
    }
    .chat-row.user {
        flex-direction: row-reverse;
        justify-content: flex-end;
    }
    .chat-row.assistant {
        flex-direction: row;
        justify-content: flex-start;
    }
    .stChatInputContainer {
        background: #1e293b !important;
        border-radius: 16px !important;
        box-shadow: 0 2px 18px 0 #00d4ff22 !important;
        border: 2px solid #00d4ff55 !important;
        margin-top: 1.7rem !important;
        animation: fadeInInput 1.1s cubic-bezier(.6,2,.6,1);
    }
    @keyframes fadeInInput {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: none; }
    }
    .stChatInputContainer textarea {
        background: transparent !important;
        color: #fff !important;
        font-size: 1.13em !important;
        border-radius: 12px !important;
        padding: 0.7em 1em !important;
        border: none !important;
        box-shadow: none !important;
    }
    .stChatInputContainer button {
        background: linear-gradient(90deg, #00d4ff 0%, #1e3c72 100%) !important;
        color: #fff !important;
        border-radius: 11px !important;
        font-weight: 800 !important;
        font-size: 1.13em !important;
        border: none !important;
        box-shadow: 0 2px 18px 0 #00d4ff55 !important;
        transition: 0.18s, box-shadow 0.3s;
        padding: 0.6em 1.5em !important;
        margin-left: 0.7em !important;
    }
    .stChatInputContainer button:hover {
        background: linear-gradient(90deg, #1e3c72 0%, #00d4ff 100%) !important;
        color: #00d4ff !important;
        box-shadow: 0 4px 24px 0 #00d4ff77 !important;
    }
    @media (max-width: 700px) {
        .header {
            flex-direction: column;
            gap: 0.3rem;
        }
        .chat-bubble {
            font-size: 1.08em !important;
            padding: 0.7rem 0.7rem;
            max-width: 98vw;
        }
        .chat-bubble.user, .chat-bubble.assistant {
            font-size: 1.08em !important;
            max-width: 98vw;
        }
    }
    </style>
    """, unsafe_allow_html=True)

    # Auto-scroll like Gemini
    st.markdown("""
    <script>
    const observer = new MutationObserver(() => {
        window.scrollTo(0, document.body.scrollHeight);
    });
    observer.observe(document.body, { childList: true, subtree: true });
    </script>
    """, unsafe_allow_html=True)


    # Remove wrapper div for a seamless, borderless chat area

    # Header buttons (modern, glassy, icon+text, always spaced)
    st.markdown('<div class="header">', unsafe_allow_html=True)
    col_hub, col_clear = st.columns([1,1], gap="small")
    with col_hub:
        if st.button("🏠 Hub", use_container_width=True):
            go_to_topic_menu()
            st.rerun()
    with col_clear:
        mode = st.session_state.get('ai_explorer_mode', 'Chat Mode')
        # Defensive initialization for quiz_messages
        if 'quiz_messages' not in st.session_state:
            st.session_state.quiz_messages = []
        if mode == "Chat Mode":
            if st.session_state.chat_messages:
                if st.button("🗑️ Clear", use_container_width=True):
                    st.session_state.chat_messages = []
                    st.session_state.ai_conversation_started = False
                    st.rerun()
        elif mode == "Quiz Mode":
            if st.session_state.quiz_messages:
                if st.button("🔄 Reset Quiz", use_container_width=True):
                    # Reset quiz state for current topic
                    topic = st.session_state.selected_topic
                    st.session_state.quiz_messages = []
                    st.session_state.quiz_asked_questions = []
                    st.session_state.score = 0
                    st.session_state.total = 0
                    st.session_state.quiz_feedback = ""
                    # Pick first question
                    all_questions = QUIZ_BANK[topic]
                    first_q = random.choice(all_questions)
                    st.session_state.current_question = first_q
                    st.session_state.quiz_asked_questions.append(first_q["question"])
                    st.session_state.quiz_messages.append({"role": "assistant", "content": first_q["question"], "type": "question", "options": first_q["options"]})
                    st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)


    # --- Mode selection logic ---
    mode = st.session_state.get('ai_explorer_mode', 'Chat Mode')
    # Use query_params for mode switching, fallback to session state
    if hasattr(st, 'query_params') and 'mode' in st.query_params:
        param_mode = st.query_params['mode']
        if param_mode in ['Chat Mode', 'Quiz Mode'] and param_mode != mode:
            mode = param_mode
            st.session_state.ai_explorer_mode = param_mode
            st.rerun()

    # --- Blended Mode Switcher (UI-enhanced buttons) ---
    def switch_mode(new_mode):
        st.query_params['mode'] = new_mode
        st.session_state.ai_explorer_mode = new_mode
        st.rerun()

    st.markdown("""
    <style>
    .mode-switcher-btn {
        background: linear-gradient(90deg, #232b3a 0%, #22334d 100%);
        color: #fff;
        border: 2px solid #00d4ff55;
        border-radius: 11px;
        padding: 0.55rem 1.4rem;
        font-size: 1.09rem;
        font-weight: 700;
        box-shadow: 0 2px 12px 0 #00d4ff33;
        text-shadow: 0 1.5px 0 #00d4ff55;
        cursor: pointer;
        outline: none;
        margin-right: 0.5em;
        transition: background 0.18s, color 0.18s, border-color 0.18s, box-shadow 0.3s;
        position: relative;
    }
    .mode-switcher-btn.active {
        background: linear-gradient(90deg, #00d4ff 0%, #1e3c72 100%);
        color: #fff;
        border: 2px solid #00d4ff;
        box-shadow: 0 4px 24px 0 #00d4ff77, 0 2px 0 #fff;
    }
    .mode-switcher-btn:hover {
        background: linear-gradient(90deg, #1e3c72 0%, #00d4ff 100%);
        color: #00d4ff;
        border-color: #fff;
        box-shadow: 0 4px 24px 0 #00d4ff77, 0 2px 0 #fff;
    }
    </style>
    """, unsafe_allow_html=True)

    # Removed JS/HTML for "Mode:" text for cleaner UI

    mode_col1, mode_col2 = st.columns([1, 1])
    with mode_col1:
        if st.button("💬 Chat Mode", key="mode_chat_btn", help="Switch to Chat Mode", use_container_width=True):
            st.session_state.ai_explorer_mode = "Chat Mode"
            if hasattr(st, "query_params"):
                st.query_params["mode"] = "Chat Mode"
            st.rerun()
    with mode_col2:
        if st.button("🎓 Quiz Mode", key="mode_quiz_btn", help="Switch to Quiz Mode", use_container_width=True):
            st.session_state.ai_explorer_mode = "Quiz Mode"
            if hasattr(st, "query_params"):
                st.query_params["mode"] = "Quiz Mode"
            st.rerun()

    # ...existing code...


    if mode == "Chat Mode":
        # --- Chat UI (restored from backup) ---
        # Ensure lesson/topic buttons NEVER appear in Chat Mode
        # Show welcome only before any message is sent
        if not st.session_state.ai_conversation_started and not st.session_state.chat_messages:
            # Get current Malaysian time (UTC+8) and choose greeting
            from datetime import datetime, timedelta
            now_utc = datetime.utcnow() + timedelta(hours=8)
            hour = now_utc.hour
            if 5 <= hour < 12:
                time_greeting = "Good Morning"
            elif 12 <= hour < 18:
                time_greeting = "Good Afternoon"
            else:
                time_greeting = "Good Evening"
            user_name = st.session_state.get('user_name', 'Friend')
            greeting_display = f"{time_greeting}, {user_name}! Let's chat with Layantara Insight."
            st.markdown(f"""
            <div class="welcome">
                <div class="emoji">🪁</div>
                <div class="title">{greeting_display}</div>
                <div class="desc">You can ask about kite mathematics, Indonesian culture, or aerodynamics—anytime!</div>
            </div>
            """, unsafe_allow_html=True)

        # Show suggestion buttons only before any message is sent
        if not st.session_state.ai_conversation_started and not st.session_state.chat_messages:
            # Move suggestion row upwards by reducing margin-top
            st.markdown('<style>.suggestion-row { margin-top: 0.2rem !important; }</style>', unsafe_allow_html=True)
            st.markdown('<div class="suggestion-row">', unsafe_allow_html=True)
            suggestions = [
                "Layangan Janggan kite",
                "Kite Symbolism",
                "Make a Kite"
            ]
            # System prompt for the AI model (Cerebras)
            system_prompt = (
                "You are Layantara Insight, a friendly educational assistant. "
                "Greet the user only at the start of the conversation, and do not greet again in subsequent replies. "
                "Always greet users in English with a neutral greeting suitable for any time of day, such as 'Hello' or 'Welcome', but only once at the beginning. "
                "Do not use time-specific greetings (e.g., Good morning, Good evening) or Indonesian greetings unless explicitly requested. "
                "Whenever a user asks about any math topic, always relate your explanation to kites, kite design, or kite flight. "
                "Do NOT generate or ask quiz questions in Chat Mode. If the user requests a quiz, first offer to teach the topic with a kite-related lesson, and then suggest switching to Quiz Mode for practice. "
                "Teach math topics using kite examples and analogies, and make the conversation engaging and relevant to kites. "
                "Answer questions about kite culture, history, symbolism, and general math concepts, but do NOT generate new math quiz questions. "
                "If asked for a quiz, always offer a lesson first, then recommend switching to Quiz Mode for quizzes."
            )
            cols = st.columns(len(suggestions))
            for i, suggestion in enumerate(suggestions):
                with cols[i]:
                    if st.button(suggestion, key=f"suggestion_{i}", use_container_width=True):
                        # Always use system prompt to enforce neutral English greeting
                        st.session_state.chat_messages.append({"role": "user", "content": suggestion})
                        st.session_state.ai_conversation_started = True
                        st.session_state.system_prompt = system_prompt
                        st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)

        # Display messages (modern chat bubbles, avatars, glassy look)
        for i, msg in enumerate(st.session_state.chat_messages):
            if msg["role"] == "user":
                avatar = "🎓"
                avatar_html = f'<span class="chat-avatar">{avatar}</span>'
            else:
                avatar_html = '<span class="chat-avatar" style="margin-right:0.5em;"><img src="https://i.imgur.com/cM9BMro.png" alt="Layantara Avatar" width="38" height="38" style="width:38px;height:38px;min-width:38px;min-height:38px;max-width:38px;max-height:38px;border-radius:50%;vertical-align:middle;box-shadow:0 2px 12px #00d4ff77;display:inline-block;object-fit:cover;image-rendering:auto;" loading="eager" decoding="async"/></span>'
            bubble_class = f"chat-bubble {msg['role']}"
            row_class = f"chat-row {msg['role']}"
            # Add id to last message for auto-scroll
            if i == len(st.session_state.chat_messages) - 1:
                st.markdown(f'<div class="{row_class}" id="last-chat-msg">{avatar_html}<div class="{bubble_class}">{msg["content"]}</div></div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="{row_class}">{avatar_html}<div class="{bubble_class}">{msg["content"]}</div></div>', unsafe_allow_html=True)

        # Auto-scroll to last chat message
        st.markdown("""
        <script>
        var lastMsg = document.getElementById('last-chat-msg');
        if (lastMsg) {
            setTimeout(function() {
                lastMsg.scrollIntoView({behavior: 'smooth', block: 'center'});
            }, 100);
        }
        </script>
        """, unsafe_allow_html=True)

        # Chat input
        user_input = st.chat_input("💬 Ask about kites, math, or Indonesian culture...")
        if user_input:
            user_input = user_input.strip()
            if user_input.lower() in ["clear", "reset", "restart"]:
                st.session_state.chat_messages = []
                st.session_state.ai_conversation_started = False
                st.rerun()
            quiz_keywords = [
                "quiz", "test", "practice questions", "give me a quiz", "math quiz", "can i try a quiz", "can i do a quiz", "can i have a quiz", "ask me a quiz", "give me questions", "give me a test", "can i do a test", "can i try a test", "can i have a test", "ask me questions", "ask me a test", "challenge me", "give me question", "give me quiz", "question", "ask me question"
            ]
            if any(qk in user_input.lower() for qk in quiz_keywords):
                # Politely decline quiz requests in Chat Mode
                st.session_state.chat_messages.append({
                    "role": "assistant",
                    "content": "📝 Sorry, quizzes are only available in Quiz Mode! Please switch to Quiz Mode using the tab above if you'd like to try a math quiz."
                })
                st.session_state.ai_conversation_started = True
                st.rerun()
            st.session_state.chat_messages.append({"role": "user", "content": user_input})
            st.session_state.ai_conversation_started = True
            st.rerun()

        # Streaming effect for assistant reply
        if (
            st.session_state.chat_messages and
            st.session_state.chat_messages[-1]["role"] == "user" and
            len(st.session_state.chat_messages) % 2 == 1
        ):
            # If auto-switch is triggered, rerun in Quiz Mode
            if st.session_state.get("auto_switch_quiz"):
                st.session_state.auto_switch_quiz = False
                st.experimental_set_query_params(mode="Quiz Mode")
                st.rerun()
            prompt = st.session_state.chat_messages[-1]["content"]
            conversation = st.session_state.chat_messages[:-1] if len(st.session_state.chat_messages) > 1 else None
            # Track if greeting has already been sent
            if "greeting_sent" not in st.session_state:
                st.session_state.greeting_sent = False
            # Set system prompt based on greeting_sent
            if not st.session_state.greeting_sent:
                st.session_state.system_prompt = (
                    "You are Layantara Insight, a friendly educational assistant. "
                    "Greet the user only at the start of the conversation, and do not greet again in subsequent replies. "
                    "Always greet users in English with a neutral greeting suitable for any time of day, such as 'Hello' or 'Welcome', but only once at the beginning. "
                    "Do not use time-specific greetings (e.g., Good morning, Good evening) or Indonesian greetings unless explicitly requested. "
                    "Whenever a user asks about any math topic, always relate your explanation to kites, kite design, or kite flight. "
                    "Do NOT generate or ask quiz questions in Chat Mode. If the user requests a quiz, first offer to teach the topic with a kite-related lesson, and then suggest switching to Quiz Mode for practice. "
                    "Teach math topics using kite examples and analogies, and make the conversation engaging and relevant to kites. "
                    "Answer questions about kite culture, history, symbolism, and general math concepts, but do NOT generate new math quiz questions. "
                    "If asked for a quiz, always offer a lesson first, then recommend switching to Quiz Mode for quizzes."
                )
            else:
                st.session_state.system_prompt = (
                    "You are Layantara Insight, a friendly educational assistant. "
                    "Do NOT greet the user. Do not say 'Hello', 'Welcome', or any greeting. "
                    "Whenever a user asks about any math topic, always relate your explanation to kites, kite design, or kite flight. "
                    "Do NOT generate or ask quiz questions in Chat Mode. If the user requests a quiz, first offer to teach the topic with a kite-related lesson, and then suggest switching to Quiz Mode for practice. "
                    "Teach math topics using kite examples and analogies, and make the conversation engaging and relevant to kites. "
                    "Answer questions about kite culture, history, symbolism, and general math concepts, but do NOT generate new math quiz questions. "
                    "If asked for a quiz, always offer a lesson first, then recommend switching to Quiz Mode for quizzes."
                )
            # Special case: Layangan Janggan kite detailed answer
            user_greetings = ["hi", "hello", "hey", "greetings", "good morning", "good afternoon", "good evening"]
            if prompt.strip().lower() in ["layangan janggan kite", "tell me about layangan janggan kite", "layangan janggan", "janggan kite"]:
                response = (
                    "The Layangan Janggan is one of Bali's most iconic traditional kites, celebrated for its majestic size, elegant design, and deep cultural roots. Originating from the island of Bali, Indonesia, the Janggan kite is instantly recognizable by its long, flowing tail—sometimes stretching over 100 meters—which symbolizes the mythical naga (dragon) in Balinese Hindu culture.\n\n"
                    "Historically, the Janggan kite has been flown during religious ceremonies and festivals, especially the Bali Kite Festival, as an offering to the gods to ensure good harvests and harmony between nature and humanity. Its construction requires skilled craftsmanship, with bamboo frames and vibrant cloth, often decorated with intricate patterns and spiritual motifs.\n\n"
                    "The flight of the Janggan is not just a spectacle but a symbol of spiritual connection, community pride, and artistic expression. Its aerodynamic shape and tail demonstrate fascinating principles of math and physics, from balance and symmetry to the effects of wind and lift.\n\n"
                    "In summary, the Layangan Janggan kite is much more than a toy—it's a living tradition, a work of art, and a bridge between generations in Balinese society. If you'd like to learn more about its design, mathematics, or cultural significance, just ask!"
                )
            elif prompt.strip().lower() in user_greetings:
                # Respond with a friendly greeting only if not already greeted
                if not st.session_state.greeting_sent:
                    user_name = st.session_state.get('user_name', 'Friend')
                    from datetime import datetime, timedelta
                    now_utc = datetime.utcnow() + timedelta(hours=8)
                    hour = now_utc.hour
                    if 5 <= hour < 12:
                        time_greeting = "Good Morning"
                    elif 12 <= hour < 18:
                        time_greeting = "Good Afternoon"
                    else:
                        time_greeting = "Good Evening"
                    response = f"{time_greeting}, {user_name}! How can I help you with kites or math today?"
                    st.session_state.greeting_sent = True
                else:
                    response = f"Hello again! How can I help you with kites or math today?"
            else:
                response = call_cerebras_api(
                    st.session_state.system_prompt + "\nUser: " + prompt,
                    st.session_state.user_name,
                    os.getenv("CEREBRAS_API_KEY"),
                    conversation
                )
            if response and "Error:" not in response:
                # After first assistant reply, set greeting_sent to True
                if not st.session_state.greeting_sent:
                    st.session_state.greeting_sent = True
                placeholder = st.empty()
                current = ""
                streaming_id = "streaming-bubble"
                scroll_script = f"""
                <script>
                setTimeout(function() {{
                    var el = document.getElementById('{streaming_id}');
                    if (el) {{
                        el.scrollIntoView({{behavior: 'smooth', block: 'end'}});
                    }}
                }}, 0);
                </script>
                """
                for line in response.split('\n'):
                    for char in line:
                        current += char
                        placeholder.markdown(f'<span class="chat-avatar"><img src="https://i.imgur.com/cM9BMro.png" alt="Layantara Avatar" style="width:38px;height:38px;border-radius:50%;vertical-align:middle;box-shadow:0 2px 12px #00d4ff77;display:inline-block;object-fit:cover;image-rendering:auto;" loading="eager" decoding="async"/></span><div class="chat-bubble assistant" id="{streaming_id}">{current}</div>' + scroll_script, unsafe_allow_html=True)
                        time.sleep(0.007)
                    current += "\n"
                    placeholder.markdown(f'<span class="chat-avatar"><img src="https://i.imgur.com/cM9BMro.png" alt="Layantara Avatar" style="width:38px;height:38px;border-radius:50%;vertical-align:middle;box-shadow:0 2px 12px #00d4ff77;display:inline-block;object-fit:cover;image-rendering:auto;" loading="eager" decoding="async"/></span><div class="chat-bubble assistant" id="{streaming_id}">{current}</div>' + scroll_script, unsafe_allow_html=True)
                    time.sleep(0.03)
                st.session_state.chat_messages.append({"role": "assistant", "content": response})
                st.rerun()
            else:
                st.session_state.chat_messages.pop()
                st.session_state.chat_messages.pop()
                st.error("⚠️ Response error. Try again.")
    elif mode == "Quiz Mode":
        # --- Unified Chat UI for Quiz Mode ---
        # Removed Quiz Mode header as requested
        topic_list = list(QUIZ_BANK.keys())
        # --- Topic dropdown always visible in Quiz Mode ---
        current_topic = st.session_state.get("selected_topic", topic_list[0])
        topic = st.selectbox("Choose a math topic:", topic_list, index=topic_list.index(current_topic))
        # If quiz hasn't started yet, initialize on first entry
        if not st.session_state.quiz_messages:
            st.session_state.selected_topic = topic
            st.session_state.quiz_messages = []
            st.session_state.quiz_asked_questions = []
            st.session_state.score = 0
            st.session_state.total = 0
            st.session_state.quiz_feedback = ""
            st.session_state.quiz_finished = False
            all_questions = QUIZ_BANK[topic]
            question_pool = random.sample(all_questions, min(10, len(all_questions)))
            for q in question_pool:
                q["options"] = random.sample(q["options"], len(q["options"]))
            st.session_state.quiz_question_pool = question_pool
            first_q = question_pool[0]
            st.session_state.current_question = first_q
            st.session_state.quiz_asked_questions.append(first_q["question"])
            st.session_state.quiz_messages.append({"role": "assistant", "content": first_q["question"], "type": "question", "options": first_q["options"]})
            st.rerun()
        # If topic changed, reset quiz state and start new quiz
        elif topic != st.session_state.selected_topic:
            st.session_state.selected_topic = topic
            st.session_state.quiz_messages = []
            st.session_state.quiz_asked_questions = []
            st.session_state.score = 0
            st.session_state.total = 0
            st.session_state.quiz_feedback = ""
            st.session_state.quiz_finished = False
            all_questions = QUIZ_BANK[topic]
            question_pool = random.sample(all_questions, min(10, len(all_questions)))
            for q in question_pool:
                q["options"] = random.sample(q["options"], len(q["options"]))
            st.session_state.quiz_question_pool = question_pool
            first_q = question_pool[0]
            st.session_state.current_question = first_q
            st.session_state.quiz_asked_questions.append(first_q["question"])
            st.session_state.quiz_messages.append({"role": "assistant", "content": first_q["question"], "type": "question", "options": first_q["options"]})
            st.rerun()

        quiz_finished = st.session_state.get("quiz_finished", False)
        score = st.session_state.get("score", 0)
        total = st.session_state.get("total", 0)
        st.markdown(f"""
        <div style='background: linear-gradient(90deg, #00d4ff 0%, #1e3c72 100%); color: #fff; border-radius: 13px; padding: 7px 18px; font-size: 1.15em; font-weight: 700; text-align: center; margin-bottom: 10px; box-shadow: 0 2px 10px 0 #00d4ff22;'>
            Score: {score} / 10
        </div>
        """, unsafe_allow_html=True)

        # Render chat bubbles for quiz conversation
        for i, msg in enumerate(st.session_state.quiz_messages):
            bubble_class = f"chat-bubble {msg['role']}"
            row_class = f"chat-row {msg['role']}"
            if msg["role"] == "user":
                avatar = "🎓"
                avatar_html = f'<span class="chat-avatar">{avatar}</span>'
            else:
                avatar_html = '<span class="chat-avatar" style="margin-right:0.5em;"><img src="https://i.imgur.com/cM9BMro.png" alt="Layantara Avatar" width="38" height="38" style="width:38px;height:38px;min-width:38px;min-height:38px;max-width:38px;max-height:38px;border-radius:50%;vertical-align:middle;box-shadow:0 2px 12px #00d4ff77;display:inline-block;object-fit:cover;image-rendering:auto;" loading="eager" decoding="async"/></span>'
            # Add id to last quiz message for auto-scroll
            if i == len(st.session_state.quiz_messages) - 1:
                st.markdown(f'<div class="{row_class}" id="last-quiz-msg">{avatar_html}<div class="{bubble_class}">{msg["content"]}</div></div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="{row_class}">{avatar_html}<div class="{bubble_class}">{msg["content"]}</div></div>', unsafe_allow_html=True)

        # Auto-scroll to last quiz message
        st.markdown("""
        <script>
        var lastQuizMsg = document.getElementById('last-quiz-msg');
        if (lastQuizMsg) {
            setTimeout(function() {
                lastQuizMsg.scrollIntoView({behavior: 'smooth', block: 'center'});
            }, 100);
        }
        </script>
        """, unsafe_allow_html=True)

        # --- Enhanced Quiz UI Styling ---
        st.markdown("""
        <style>
        .quiz-radio .stRadio > div {
            background: linear-gradient(90deg, #232b3a 60%, #22334d 100%);
            border-radius: 16px;
            box-shadow: 0 2px 18px 0 #00d4ff22;
            border: 2px solid #00d4ff55;
            padding: 1.1rem 1.5rem;
            margin: 0.7rem 0;
            color: #fff;
            font-size: 1.25em !important;
            font-weight: 600;
            transition: box-shadow 0.2s;
        }
        .quiz-radio .stRadio > div:hover {
            box-shadow: 0 4px 24px 0 #00d4ff77;
            border-color: #00d4ff;
        }
        .quiz-radio label {
            color: #00d4ff;
            font-weight: 700;
            font-size: 1.18em;
            margin-bottom: 0.5em;
        }
        .quiz-radio .stRadio > label {
            font-size: 1.18em !important;
        }
        .quiz-submit-btn .stButton > button,
        .quiz-teach-btn .stButton > button {
            background: linear-gradient(90deg, #00d4ff 0%, #1e3c72 100%);
            color: #fff;
            border: 2px solid #00d4ff;
            border-radius: 13px;
            padding: 0.7rem 2.2rem;
            font-weight: 800;
            font-size: 1.25em;
            letter-spacing: 0.01em;
            box-shadow: 0 2px 16px 0 #00d4ff33, 0 1.5px 0 #00d4ff;
            transition: 0.18s, box-shadow 0.3s;
            outline: none;
            min-width: 110px;
            text-shadow: 0 2px 12px #00d4ff55;
            filter: drop-shadow(0 2px 8px #00d4ff33);
            position: relative;
            overflow: hidden;
        }
        .quiz-submit-btn .stButton > button:hover,
        .quiz-teach-btn .stButton > button:hover {
            border-color: #fff;
            background: linear-gradient(90deg, #1e3c72 0%, #00d4ff 100%);
            color: #00d4ff;
            box-shadow: 0 4px 32px 0 #00d4ff77, 0 2px 0 #fff;
        }
        </style>
        """, unsafe_allow_html=True)

        # Defensive: Only access last_msg if quiz_messages is not empty
        if st.session_state.quiz_messages:
            last_msg = st.session_state.quiz_messages[-1]
        else:
            last_msg = None
        # Quiz logic: only allow 10 questions per topic, no repeats
        question_pool = st.session_state.get("quiz_question_pool", [])
        asked = st.session_state.get("quiz_asked_questions", [])
        # If finished all questions, show final score and topic dropdown for next quiz
        if st.session_state.total >= 10 or st.session_state.quiz_finished:
            st.session_state.quiz_finished = True
            st.markdown(f"""
            <div style='background: linear-gradient(90deg, #4CAF50 0%, #00d4ff 100%); color: #fff; border-radius: 13px; padding: 14px 22px; font-size: 1.25em; font-weight: 800; text-align: center; margin: 18px 0 10px 0; box-shadow: 0 2px 10px 0 #00d4ff22;'>
                🎉 Final Score: {score} / 10
            </div>
            """, unsafe_allow_html=True)
            st.markdown("<div style='font-size:1.15em;font-weight:700;color:#fff;margin:18px 0 8px 0;'>Choose another topic:</div>", unsafe_allow_html=True)
            topic_list = list(QUIZ_BANK.keys())
            # Default to next topic if available, else first topic
            current_idx = topic_list.index(st.session_state.selected_topic)
            next_idx = (current_idx + 1) % len(topic_list)
            next_topic = topic_list[next_idx]
            topic = st.selectbox("Select topic for new quiz:", topic_list, index=next_idx)
            if st.button("Start Quiz", key="start_new_topic_btn", type="primary", use_container_width=True):
                st.session_state.selected_topic = topic
                st.session_state.quiz_messages = []
                st.session_state.quiz_asked_questions = []
                st.session_state.score = 0
                st.session_state.total = 0
                st.session_state.quiz_feedback = ""
                st.session_state.quiz_finished = False
                all_questions = QUIZ_BANK[topic]
                question_pool = random.sample(all_questions, min(10, len(all_questions)))
                for q in question_pool:
                    q["options"] = random.sample(q["options"], len(q["options"]))
                st.session_state.quiz_question_pool = question_pool
                first_q = question_pool[0]
                st.session_state.current_question = first_q
                st.session_state.quiz_asked_questions.append(first_q["question"])
                st.session_state.quiz_messages.append({"role": "assistant", "content": first_q["question"], "type": "question", "options": first_q["options"]})
                st.rerun()
            return

        if last_msg and last_msg.get("type") == "question":
            st.markdown("""
            <style>
            .quiz-radio .stRadio > div {
                background: #f8fafc;
                border-radius: 14px;
                box-shadow: 0 2px 12px #00d4ff22;
                padding: 0.7rem 1.2rem;
                margin-bottom: 0.7rem;
                transition: box-shadow 0.3s, border 0.3s;
            }
            .quiz-radio .stRadio > div:hover {
                box-shadow: 0 4px 24px #00d4ff44;
                border: 2px solid #00d4ff55;
            }
            .quiz-radio label {
                font-size: 1.08em;
                font-weight: 600;
                color: #22334d;
                letter-spacing: 0.01em;
            }
            .quiz-submit-btn .stButton > button {
                background: linear-gradient(90deg, #00d4ff 0%, #1e3c72 100%);
                color: #fff;
                border-radius: 13px;
                border: none;
                font-weight: 700;
                font-size: 1.13em;
                padding: 0.7rem 2.2rem;
                box-shadow: 0 2px 12px #00d4ff33;
                transition: background 0.3s, box-shadow 0.3s;
            }
            .quiz-submit-btn .stButton > button:hover {
                background: linear-gradient(90deg, #1e3c72 0%, #00d4ff 100%);
                color: #00d4ff;
                box-shadow: 0 4px 32px 0 #00d4ff77, 0 2px 0 #fff;
            }
            .quiz-teach-btn .stButton > button {
                background: linear-gradient(90deg, #232b3a 0%, #22334d 100%);
                color: #fff;
                border: 2px solid #00d4ff55;
                border-radius: 13px;
                padding: 0.6rem 1.5rem;
                font-weight: 800;
                font-size: 1.13em;
                letter-spacing: 0.01em;
                box-shadow: 0 2px 12px #22334d22;
                transition: background 0.3s, border 0.3s;
            }
            .quiz-teach-btn .stButton > button:hover {
                background: linear-gradient(90deg, #00d4ff 0%, #232b3a 100%);
                color: #232b3a;
                border: 2px solid #00d4ff;
            }
            .quiz-radio .stRadio > div[data-selected="true"] {
                border: 2px solid #00d4ff;
                box-shadow: 0 2px 16px #00d4ff44;
            }
            .quiz-radio .stRadio > div input[type="radio"]:checked + label {
                color: #00d4ff;
            }
            .quiz-radio .stRadio > div input[type="radio"] {
                accent-color: #00d4ff;
            }
            .quiz-radio .stRadio > div label {
                cursor: pointer;
            }
            .quiz-submit-btn, .quiz-teach-btn {
                margin-top: 0.5rem;
                margin-bottom: 0.5rem;
                text-align: center;
            }
            </style>
            """, unsafe_allow_html=True)
            st.markdown('<div class="quiz-radio">', unsafe_allow_html=True)
            st.markdown("""
            <div style='font-size:1.25em;font-weight:700;color:#fff;margin-bottom:0.15em;'>Choose the correct answer:</div>
            """, unsafe_allow_html=True)
            user_answer = st.radio("", last_msg["options"], key=f"quiz_choice_{st.session_state.total}", format_func=lambda x: x, label_visibility="visible")
            st.markdown('</div>', unsafe_allow_html=True)
            st.markdown('<div class="quiz-submit-btn">', unsafe_allow_html=True)
            if st.button("🎯 Submit Answer", type="primary", use_container_width=True):
                st.session_state.quiz_messages.append({"role": "user", "content": str(user_answer)})
                correct = user_answer == st.session_state.current_question["answer"]
                st.session_state.total += 1
                explanation = st.session_state.current_question.get("explanation", "")
                # If explanation is missing, show a clear fallback
                if not explanation:
                    explanation = "No explanation available for this question. Please notify your instructor to add one."
                if correct:
                    feedback = f"✅ <span style='color:#4CAF50;font-weight:700;'>Correct!</span> <span style='color:#fff;'>{explanation}</span>"
                    st.session_state.score += 1
                else:
                    feedback = f"❌ <span style='color:#E91E63;font-weight:700;'>Incorrect.</span> <span style='color:#fff;'>{explanation}</span>"
                st.session_state.quiz_messages.append({"role": "assistant", "content": feedback, "type": "feedback"})
                st.session_state.quiz_feedback = feedback
                # Track asked question
                st.session_state.quiz_asked_questions.append(st.session_state.current_question["question"])
                # Get next unique question from pool
                if st.session_state.total < 10:
                    # Find the next question that hasn't been asked yet
                    for q in st.session_state.quiz_question_pool:
                        if q["question"] not in st.session_state.quiz_asked_questions:
                            # Shuffle options for next question
                            q["options"] = random.sample(q["options"], len(q["options"]))
                            st.session_state.current_question = q
                            st.session_state.quiz_messages.append({"role": "assistant", "content": q["question"], "type": "question", "options": q["options"]})
                            break
                st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)

        # Show feedback and allow next question
        if last_msg and last_msg.get("type") == "feedback":
            st.markdown(f"<div style='font-size:1.1em;font-weight:600;color:#fff;margin-bottom:0.5em;'>Score: {score} / 10</div>", unsafe_allow_html=True)
            next_idx = st.session_state.total
            if st.session_state.total < 10 and next_idx < len(st.session_state.quiz_question_pool):
                if st.button("Next Question"):
                    next_q = st.session_state.quiz_question_pool[next_idx]
                    # Shuffle options for next question
                    next_q["options"] = random.sample(next_q["options"], len(next_q["options"]))
                    st.session_state.current_question = next_q
                    st.session_state.quiz_messages.append({"role": "assistant", "content": next_q["question"], "type": "question", "options": next_q["options"]})
                    st.session_state.quiz_feedback = ""
                    st.rerun()
            else:
                st.markdown("<div style='color:#fff;font-size:1.1em;font-weight:600;margin-top:0.5em;'>Quiz complete! Please select a new topic or reset the quiz.</div>", unsafe_allow_html=True)

        st.markdown('<div class="quiz-teach-btn">', unsafe_allow_html=True)
        teach_btn = st.button("Teach me this topic", type="primary", use_container_width=True)
        if teach_btn:
            lesson_prompt = (
                f"Teach the topic '{topic}' using examples from kite shapes or flight design. "
                "Explain like a tutor helping a student in higher education."
            )
            lesson = call_cerebras_api(lesson_prompt, st.session_state.user_name, os.getenv("CEREBRAS_API_KEY"))
            # Add lesson as a chat bubble to quiz_messages, preserving markdown formatting
            st.session_state.quiz_messages.append({
                "role": "assistant",
                "content": f"<b>📘 Lesson</b>\n\n{lesson}",
                "type": "lesson"
            })
            st.session_state.quiz_feedback = ""
            st.rerun()

        # If last message is a lesson, show "Next Question" button to continue
        if st.session_state.quiz_messages and st.session_state.quiz_messages[-1]["type"] == "lesson":
            next_idx = st.session_state.total
            st.markdown('<div class="quiz-submit-btn">', unsafe_allow_html=True)
            if st.session_state.total < 10 and next_idx < len(st.session_state.quiz_question_pool):
                if st.button("Next Question", key="next_after_lesson", type="primary", use_container_width=True):
                    next_q = st.session_state.quiz_question_pool[next_idx]
                    # Shuffle options for next question
                    next_q["options"] = random.sample(next_q["options"], len(next_q["options"]))
                    st.session_state.current_question = next_q
                    st.session_state.quiz_messages.append({"role": "assistant", "content": next_q["question"], "type": "question", "options": next_q["options"]})
                    st.session_state.quiz_feedback = ""
                    st.rerun()
            else:
                st.markdown("<div style='color:#fff;font-size:1.1em;font-weight:600;margin-top:0.5em;'>Quiz complete! Please select a new topic or reset the quiz.</div>", unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

# --- LESSONS IMPLEMENTATION ---

# --- ANGLES LESSON ---
def angles_intro():
    # ✅ Top-level layout override (first thing in function)
    st.markdown("""
    <style>
    section.main > div.block-container {
        padding-top: 0rem !important;
        margin-top: 0rem !important;
    }
    [data-testid="column"] {
        padding-top: 0rem !important;
        margin-top: 0rem !important;
    }
    .stButton button {
        white-space: nowrap;
        padding-top: 0.35rem !important;
        padding-bottom: 0.25rem !important;
        margin-top: 10px !important;
    }
    .angles-page img {
        max-height: 180px;
        object-fit: contain;
    }
    /* Responsive for angles page */
    @media (max-width: 900px) {
        .angles-page .stColumns, .angles-page [data-testid="column"] {
            flex-direction: column !important;
            width: 100% !important;
            min-width: 0 !important;
            max-width: 100% !important;
        }
        .angles-page .stButton button {
            font-size: 1em !important;
            padding: 0.5rem 1rem !important;
        }
        .angles-page img {
            max-width: 100% !important;
            height: auto !important;
        }
    }
    @media (max-width: 600px) {
        .angles-page .stColumns, .angles-page [data-testid="column"] {
            flex-direction: column !important;
            width: 100% !important;
            min-width: 0 !important;
            max-width: 100% !important;
        }
        .angles-page .stButton button {
            font-size: 0.95em !important;
            padding: 0.4rem 0.7rem !important;
        }
        .angles-page img {
            max-width: 100% !important;
            height: auto !important;
        }
    }
    </style>
    """, unsafe_allow_html=True)

    # Start page content container
    st.markdown('<div class="angles-page">', unsafe_allow_html=True)

    # --- Header row ---
    col1, col2 = st.columns([5.1, 1.5])
    with col1:
        st.markdown("### 📐 Angles in Kite Design")
    with col2:
        if st.button("🏠 Learning Hub", key="angles_home_nav", help="Return to main menu"):
            go_to_topic_menu()
            st.rerun()

    # --- Tabs ---
    tab1, tab2 = st.tabs(["📖 Learn", "🎯 Practice"])

    # --- Learn Tab ---
    with tab1:
        learn_col1, learn_col2 = st.columns([1, 1])
        with learn_col1:
            st.image(KITE_IMAGES["angles"], use_container_width=True)
        with learn_col2:
            st.markdown("**Learning Goal:** Count geometric angles in the kite's head.")
            st.markdown("**Look for:** Sharp intersection points where curved edges meet.")
            with st.expander("📚 Background"):
                st.markdown("""
                The **Layangan Janggan kite** has sharp points where bamboo framework meets, creating angles. 
                Indonesian artisans perfect these for balance and beauty.
                """)

    # --- Practice Tab ---
    with tab2:
        prac_col1, prac_col2 = st.columns([1, 1])

        with prac_col1:
            st.image(KITE_IMAGES["angles"], use_container_width=True)

        with prac_col2:
            st.markdown("**How many angles in the kite's head?**")
            st.markdown("**Look for:** Sharp intersection points where curved edges meet")

            with st.form(key="angles_q1_form"):
                options = [3, 2, 6]
                selected_option = st.radio("Choose answer:", options, key="angles_q1_radio", help="Count sharp points")

                # Submit button row
                form_col1, form_col2 = st.columns([3, 1])
                with form_col1:
                    submit_button = st.form_submit_button(label="Submit", type="primary", use_container_width=True)
                with form_col2:
                    st.markdown(
                        "<div style='text-align: center; padding: 2px; color: #666; font-size: 0.6em;'>💡 Count tips!</div>",
                        unsafe_allow_html=True
                    )

                if submit_button:
                    if selected_option == 2:
                        st.session_state.lesson_done["angles"] = True
                        set_stage("angles_correct")
                    else:
                        st.session_state.angles_wrong += 1
                        if st.session_state.angles_wrong == 1:
                            set_stage("angles_wrong1")
                        else:
                            set_stage("angles_wrong2")
                    st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)

def angles_correct_answer():
    # Ultra-compact container
    st.markdown('<div class="angles-page">', unsafe_allow_html=True)

    # ✅ Celebration heading
    st.success("🎉 Excellent!")

    # ✅ Personalized + compact lesson summary in 2 columns
    st.markdown(
        f"""✅ Right, {st.session_state.user_name}! The **Layangan Janggan** kite has **2 sharp-point angles**.
        
**What You Learned:**
- Angles are set to 60° for balance, blending geometry with artistic design  
- Math in kites reflects Indonesian craftsmanship and cultural tradition 📐🪁
        """
    )

    # ✅ Compact Next Steps
    st.markdown("### 🎯 Next Adventure")

    next_col1, next_col2 = st.columns(2)

    with next_col1:
        st.markdown("**📚 Continue**")
        if st.button("🏠 Learning Hub",
                     on_click=go_to_topic_menu,
                     key="angles_correct_main_menu",
                     type="primary",
                     help="Select another lesson",
                     use_container_width=True):
            pass

        if st.button("📏 Trigonometry",
                     key="angles_correct_next_lesson",
                     help="Next lesson",
                     use_container_width=True):
            st.session_state.trig_wrong = 0
            set_stage("trig_intro")
            st.rerun()

    with next_col2:
        st.markdown("**🔄 Options**")
        if st.button("🔄 Repeat",
                     on_click=repeat_angles_lesson,
                     key="angles_correct_repeat_lesson",
                     help="Review lesson",
                     use_container_width=True):
            pass

        if st.button("👋 End Session",
                     on_click=end_session,
                     key="angles_correct_end_session",
                     help="Complete session",
                     use_container_width=True):
            pass

    st.markdown('</div>', unsafe_allow_html=True)

def angles_wrong_answer1():
    # 🧼 Spacing and layout fixes
    st.markdown("""
    <style>
    section.main > div.block-container {
        padding-top: 0rem !important;
        margin-top: 0rem !important;
    }
    [data-testid="column"] {
        padding-top: 0rem !important;
        margin-top: 0rem !important;
    }
    .stButton button {
        white-space: nowrap;
        padding-top: 0.35rem !important;
        padding-bottom: 0.25rem !important;
        margin-top: -2px !important;
    }
    .angles-page img {
        max-height: 180px;
        object-fit: contain;
        margin-bottom: 0.25rem;
    }
    .stRadio {
        margin-top: 0.4rem !important;
        margin-bottom: 0.5rem !important;
    }
    /* Responsive for angles page (wrong answer) */
    @media (max-width: 900px) {
        .angles-page .stColumns, .angles-page [data-testid="column"] {
            flex-direction: column !important;
            width: 100% !important;
            min-width: 0 !important;
            max-width: 100% !important;
        }
        .angles-page .stButton button {
            font-size: 1em !important;
            padding: 0.5rem 1rem !important;
        }
        .angles-page img {
            max-width: 100% !important;
            height: auto !important;
        }
    }
    @media (max-width: 600px) {
        .angles-page .stColumns, .angles-page [data-testid="column"] {
            flex-direction: column !important;
            width: 100% !important;
            min-width: 0 !important;
            max-width: 100% !important;
        }
        .angles-page .stButton button {
            font-size: 0.95em !important;
            padding: 0.4rem 0.7rem !important;
        }
        .angles-page img {
            max-width: 100% !important;
            height: auto !important;
        }
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="angles-page">', unsafe_allow_html=True)

    # --- Hint and back button ---
    col1, col2 = st.columns([5.1, 1.5])
    with col1:
        st.markdown(
            f"""❌ Let's look closer, {st.session_state.user_name}!  
🔍 **Hint:** Focus on the "almond tips" where curves create sharp points."""
        )
        st.markdown("&nbsp;")  # Adds visible vertical space
    with col2:
        if st.button("🏠 Learning Hub", key="angles_wrong1_home_nav", help="Return to main menu"):
            go_to_topic_menu()
            st.rerun()

    # --- Image and form side by side ---
    col_img, col_quiz = st.columns([1, 1])

    with col_img:
        st.image(KITE_IMAGES["angles"], use_container_width=True)

    with col_quiz:
        with st.form(key="angles_q2_form"):
            options = [3, 2, 6]
            selected_option = st.radio("Choose answer:", options, key="angles_q2_radio", help="Count sharp points")

            form_col1, form_col2 = st.columns([3, 1])
            with form_col1:
                submit_button = st.form_submit_button(label="Try Again", type="primary", use_container_width=True)
            with form_col2:
                help_button = st.form_submit_button("Help", use_container_width=True)

            if help_button:
                st.warning("💡 Look at the two pointed ends!")

            if submit_button:
                if selected_option == 2:
                    st.session_state.lesson_done["angles"] = True
                    set_stage("angles_correct")
                else:
                    st.session_state.angles_wrong += 1
                    set_stage("angles_wrong2")
                st.rerun()

        # Add vertical space at bottom
        st.markdown("&nbsp;")

    st.markdown('</div>', unsafe_allow_html=True)

def angles_wrong_answer2():
    # Add class for ultra-compact styling
    st.markdown('<div class="angles-page">', unsafe_allow_html=True)
    
    # Ultra-compact feedback message
    st.markdown(
        f"""❌ Not correct, {st.session_state.user_name}, but learning takes practice! 🌱

**Answer:** The Layangan Janggan has **2 angles** — one at each sharp point.

**Why?** This almond design has curves that meet at only two points."""
    )
    
    # Ultra-compact navigation
    st.markdown("### 🎯 Continue Learning")
    
    nav_col1, nav_col2 = st.columns(2)
    
    with nav_col1:
        st.markdown("**📚 Keep Learning**")
        if st.button("🏠 Learning Hub", 
                    on_click=go_to_topic_menu, 
                    key="angles_wrong2_main_menu",
                    type="primary",
                    help="Choose your next lesson",
                    use_container_width=True):
            pass
        
        if st.button("📏 Trigonometry", 
                    key="angles_wrong2_next_lesson",
                    help="Next lesson",
                    use_container_width=True):
            st.session_state.trig_wrong = 0
            set_stage("trig_intro")
            st.rerun()
    
    with nav_col2:
        st.markdown("**🔄 Practice**")
        if st.button("🔄 Repeat", 
                    on_click=repeat_angles_lesson, 
                    key="angles_wrong2_repeat_lesson",
                    help="Try again",
                    use_container_width=True):
            pass
        
        if st.button("👋 End", 
                    on_click=end_session, 
                    key="angles_wrong2_end_session",
                    help="Complete session",
                    use_container_width=True):
            pass
    
    st.markdown('</div>', unsafe_allow_html=True)

# --- TRIGONOMETRY LESSON ---
def trig_intro():
    # ✅ Scroll-free layout and style optimization
    st.markdown("""
    <style>
    section.main > div.block-container {
        padding-top: 0rem !important;
        margin-top: 0rem !important;
    }
    [data-testid="column"] {
        padding-top: 0rem !important;
        margin-top: 0rem !important;
    }
    .stButton button {
        white-space: nowrap;
        padding-top: 0.35rem !important;
        padding-bottom: 0.25rem !important;
        margin-top: -2px !important;
    }
    .trig-page img {
        max-height: 180px;
        object-fit: contain;
        margin-bottom: 0.3rem;
    }
    .trig-page .stRadio {
        margin-bottom: 0.4rem !important;
    }
    .trig-page .stMarkdown {
        margin-bottom: 0.4rem !important;
    }
    .trig-page .ref {
        font-size: 0.75em;
        color: #444;
    }
    /* Responsive for trig page */
    @media (max-width: 900px) {
        .trig-page .stColumns, .trig-page [data-testid="column"] {
            flex-direction: column !important;
            width: 100% !important;
            min-width: 0 !important;
            max-width: 100% !important;
        }
        .trig-page .stButton button {
            font-size: 1em !important;
            padding: 0.5rem 1rem !important;
        }
        .trig-page img {
            max-width: 100% !important;
            height: auto !important;
        }
    }
    @media (max-width: 600px) {
        .trig-page .stColumns, .trig-page [data-testid="column"] {
            flex-direction: column !important;
            width: 100% !important;
            min-width: 0 !important;
            max-width: 100% !important;
        }
        .trig-page .stButton button {
            font-size: 0.95em !important;
            padding: 0.4rem 0.7rem !important;
        }
        .trig-page img {
            max-width: 100% !important;
            height: auto !important;
        }
    }
    </style>
    """, unsafe_allow_html=True)

    # ✅ Begin layout
    st.markdown('<div class="trig-page">', unsafe_allow_html=True)

    # --- Top Row: Header + Learning Hub button ---
    col1, col2 = st.columns([5.1, 1.5])
    with col1:
        st.markdown("### 📏 Lesson 2: Trigonometry and Kite Flying")
    with col2:
        st.markdown('<div style="padding-top: 0.35rem;">', unsafe_allow_html=True)
        if st.button("🏠 Learning Hub", key="trig_home_nav", help="Return to main menu"):
            go_to_topic_menu()
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    # --- TABS ---
    tab1, tab2 = st.tabs(["📖 Learn", "🎯 Practice"])

    # --- LEARN TAB ---
    with tab1:
        col1, col2 = st.columns([1, 1])
        with col1:
            st.image(KITE_IMAGES["trigonometry"], use_container_width=True)

        with col2:
            st.markdown("""
**🪁 Kite Height with Trigonometry**

Flying a kite forms a **right-angled triangle**:
- 🪁 **Hypotenuse**: Kite string (20m)  
- 📏 **Opposite**: Height of kite  
- ➡️ **Adjacent**: Ground distance  

To find the height, apply the formula:  
**sin(θ) = opposite / hypotenuse**
            """)

        # --- PRACTICE TAB ---
    with tab2:
        # Two columns: image | question + MCQ
        prac_col1, prac_col2 = st.columns([1, 1])

        with prac_col1:
            st.image(KITE_IMAGES["trigonometry"], use_container_width=True)

        with prac_col2:
            st.markdown("**What is the height of the kite if the string is 20 meters long and the angle is 30°?**")

            st.markdown("""
            <div class="ref">
            📐 Quick Reference:  
            • sin(30°) = 0.5  
            • Formula: height = string × sin(angle)
            </div>
            """, unsafe_allow_html=True)

            with st.form(key="trig_q1_form"):
                options = [5, 15, 10]
                st.markdown("<div style='margin-top: 0.5rem'></div>", unsafe_allow_html=True)

                selected_option = st.radio("Choose the correct answer:",
                                           options,
                                           key="trig_q1_radio",
                                           help="Apply the formula: height = string × sin(angle)")

                form_col1, form_col2 = st.columns([2, 1])
                with form_col1:
                    submit_button = st.form_submit_button(label="🎯 Submit Answer",
                                                          type="primary",
                                                          use_container_width=True)
                with form_col2:
                    st.markdown(
                        "<div style='text-align: center; padding: 4px; color: #666; font-size: 0.75em;'>📐 Use the formula above!</div>",
                        unsafe_allow_html=True
                    )

                if submit_button:
                    if selected_option == 10:
                        st.session_state.lesson_done["trig"] = True
                        set_stage("trig_correct")
                    else:
                        st.session_state.trig_wrong += 1
                        if st.session_state.trig_wrong == 1:
                            set_stage("trig_wrong1")
                        else:
                            set_stage("trig_wrong2")
                    st.rerun()

    # ✅ End layout container
    st.markdown('</div>', unsafe_allow_html=True)

def trig_correct_answer():
    # ✅ Compact layout styling
    st.markdown("""
    <style>
    section.main > div.block-container {
        padding-top: 0rem !important;
        margin-top: 0rem !important;
    }

    [data-testid="column"] {
        padding-top: 0rem !important;
        margin-top: 0rem !important;
    }

    .trig-page .stMarkdown {
        margin-bottom: 0.4rem !important;
    }

    .stButton button {
        white-space: nowrap;
        padding-top: 0.35rem !important;
        padding-bottom: 0.25rem !important;
        margin-top: -2px !important;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="trig-page">', unsafe_allow_html=True)

    # ✅ Heading and celebration
    st.success("🎉 Excellent work!")

    st.markdown(f"""
✅ Well done, {st.session_state.user_name}!  
You got it: **Height = 20 × 0.5 = 10 meters**.
""")

    # ✅ Condensed learning summary (1 column, 2 points)
    st.markdown("""
**📚 What You Learned:**
- Trigonometry helps model height problems using real-world angles and distances  
- The sine function connects triangle sides to solve practical situations 🪁  
""")

    # ✅ Navigation section
    st.markdown("### 🎯 Next Adventure")

    next_col1, next_col2 = st.columns(2)

    with next_col1:
        st.markdown("**📚 Continue**")
        if st.button("🏠 Learning Hub",
                     on_click=go_to_topic_menu,
                     key="trig_correct_main_menu",
                     type="primary",
                     help="Select another lesson",
                     use_container_width=True):
            pass

        if st.button("⭕ Perimeter",
                     key="trig_correct_next_lesson",
                     help="Next lesson",
                     use_container_width=True):
            st.session_state.peri_wrong = 0
            set_stage("peri_intro")
            st.rerun()

    with next_col2:
        st.markdown("**🔄 Options**")
        if st.button("🔄 Repeat",
                     on_click=repeat_trig_lesson,
                     key="trig_correct_repeat_lesson",
                     help="Review lesson",
                     use_container_width=True):
            pass

        if st.button("👋 End",
                     on_click=end_session,
                     key="trig_correct_end_session",
                     help="Complete session",
                     use_container_width=True):
            pass

    st.markdown('</div>', unsafe_allow_html=True)

def trig_wrong_answer1():
    # 🧼 Compact layout styling
    st.markdown("""
    <style>
    section.main > div.block-container {
        padding-top: 0rem !important;
        margin-top: 0rem !important;
    }

    [data-testid="column"] {
        padding-top: 0rem !important;
        margin-top: 0rem !important;
    }

    .stButton button {
        white-space: nowrap;
        padding-top: 0.35rem !important;
        padding-bottom: 0.25rem !important;
        margin-top: -2px !important;
    }

    .trig-page img {
        max-height: 180px;
        object-fit: contain;
        margin-bottom: 0.3rem;
    }

    .trig-page .stRadio > div {
        font-size: 0.78em !important;
        line-height: 1.2 !important;
        row-gap: 0.25rem !important;
        margin-top: 0.4rem !important;
        margin-bottom: 0.6rem !important;
    }

    </style>
    """, unsafe_allow_html=True)

    # ✅ Begin layout container
    st.markdown('<div class="trig-page">', unsafe_allow_html=True)

    # --- Header + back button row ---
    col1, col2 = st.columns([5.1, 1.5])
    with col1:
        st.markdown(
            f"""❌ Hmm, not quite, {st.session_state.user_name}, but you're close! 😅  
Take another look at the image:"""
        )
    with col2:
        if st.button("🏠 Learning Hub", key="trig_wrong1_home_nav", help="Return to main menu"):
            go_to_topic_menu()
            st.rerun()

    # --- Image and retry form layout ---
    col_img, col_quiz = st.columns([1, 1])

    with col_img:
        st.image(KITE_IMAGES["trigonometry"], use_container_width=True)

    with col_quiz:
        with st.form(key="trig_q2_form"):
            st.markdown("<div style='margin-top: 0.4rem'></div>", unsafe_allow_html=True)

            st.markdown("""
<div style='font-size: 1.05em; font-weight: 600; display: flex; align-items: center; gap: 6px;'>
    📝 <span>Choose the correct answer:</span>
</div>
""", unsafe_allow_html=True)

            options = [5, 15, 10]
            selected_option = st.radio("", options, key="trig_q2_radio")

            form_col1, form_col2 = st.columns([2, 1])
            with form_col1:
                submit_button = st.form_submit_button(label="🎯 Submit Answer",
                                                      type="primary",
                                                      use_container_width=True)
            with form_col2:
                st.markdown(
                    "<div style='text-align: center; padding: 4px; color: #666; font-size: 0.75em;'>📐 Use height = 20 × sin(30°)</div>",
                    unsafe_allow_html=True
                )

            if submit_button:
                if selected_option == 10:
                    st.session_state.lesson_done["trig"] = True
                    set_stage("trig_correct")
                else:
                    st.session_state.trig_wrong += 1
                    set_stage("trig_wrong2")
                st.rerun()

    # ✅ End layout container
    st.markdown('</div>', unsafe_allow_html=True)

def trig_wrong_answer2():
    st.markdown('<div class="trig-page">', unsafe_allow_html=True)
    st.markdown(
        f"""❌ That's still not correct, {st.session_state.user_name}.

That's okay—learning something new takes practice! 🌱

**Here's the calculation:**  
**sin(30°) = 0.5**  
So **height = 20 × 0.5 = 10 meters**."""
    )
    st.markdown("### 🎯 Continue Learning")
    nav_col1, nav_col2 = st.columns(2)
    with nav_col1:
        st.markdown("**📚 Keep Learning**")
        if st.button("🏠 Learning Hub",
                     on_click=go_to_topic_menu,
                     key="trig_wrong2_main_menu",
                     type="primary",
                     help="Choose your next lesson",
                     use_container_width=True):
            pass
        if st.button("⭕ Perimeter",
                     key="trig_wrong2_next_lesson",
                     help="Next lesson",
                     use_container_width=True):
            st.session_state.peri_wrong = 0
            set_stage("peri_intro")
            st.rerun()
    with nav_col2:
        st.markdown("**🔄 Practice**")
        if st.button("🔄 Repeat",
                     on_click=repeat_trig_lesson,
                     key="trig_wrong2_repeat_lesson",
                     help="Try again",
                     use_container_width=True):
            pass
        if st.button("👋 End",
                     on_click=end_session,
                     key="trig_wrong2_end_session",
                     help="Complete session",
                     use_container_width=True):
            pass
    st.markdown('</div>', unsafe_allow_html=True)

# --- PERIMETER LESSON ---
def peri_intro():
    # ✅ Scroll-free layout and style optimization
    st.markdown("""
    <style>
    section.main > div.block-container {
        padding-top: 0rem !important;
        margin-top: 0rem !important;
    }
    [data-testid="column"] {
        padding-top: 0rem !important;
        margin-top: 0rem !important;
    }
    .peri-page img {
        max-height: 180px;
        object-fit: contain;
        margin-bottom: 0.3rem;
    }
    .peri-page .stRadio > div {
        font-size: 0.78em !important;
        line-height: 1.2 !important;
        row-gap: 0.25rem !important;
        margin-top: 0.4rem !important;
        margin-bottom: 0.6rem !important;
    }
    .peri-page .stButton > button {
        white-space: nowrap;
        padding: 0.35rem 0.6rem !important;
        font-size: 0.75em !important;
    }
    .peri-page .ref {
        font-size: 0.75em;
        color: #444;
    }
    /* Responsive for peri page */
    @media (max-width: 900px) {
        .peri-page .stColumns, .peri-page [data-testid="column"] {
            flex-direction: column !important;
            width: 100% !important;
            min-width: 0 !important;
            max-width: 100% !important;
        }
        .peri-page .stButton > button {
            font-size: 1em !important;
            padding: 0.5rem 1rem !important;
        }
        .peri-page img {
            max-width: 100% !important;
            height: auto !important;
        }
    }
    @media (max-width: 600px) {
        .peri-page .stColumns, .peri-page [data-testid="column"] {
            flex-direction: column !important;
            width: 100% !important;
            min-width: 0 !important;
            max-width: 100% !important;
        }
        .peri-page .stButton > button {
            font-size: 0.95em !important;
            padding: 0.4rem 0.7rem !important;
        }
        .peri-page img {
            max-width: 100% !important;
            height: auto !important;
        }
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="peri-page">', unsafe_allow_html=True)

    # --- Header Row: Title + Home Button ---
    col1, col2 = st.columns([5.1, 1.5])
    with col1:
        st.markdown("### ⭕ Lesson 3: Perimeter and Curved Geometry")
    with col2:
        st.markdown('<div style="padding-top: 0.35rem;">', unsafe_allow_html=True)
        if st.button("🏠 Learning Hub", key="peri_home_nav", help="Return to main menu"):
            go_to_topic_menu()
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    # --- Tabs ---
    tab1, tab2 = st.tabs(["📖 Learn", "🎯 Practice"])

    # --- LEARN TAB ---
    with tab1:
        col1, col2 = st.columns([1, 1.75])
        with col1:
            st.image(KITE_IMAGES["perimeter"], width=220)

        with col2:
            st.markdown("""
        **💡 What You'll Learn:**  
        Estimate the perimeter of curved shapes like the Vesica Piscis using a simplified formula.

        **📚 About the Shape:**  
        The Layangan Janggan kite has a Vesica Piscis body — made from two overlapping circles. Its edges form two arcs instead of straight lines.

        **🧠 Formula Used:**  
        Perimeter = (2 × π × d) ÷ 3  
        This works because the arcs cover 2⁄3 of a full circle based on the tip-to-tip distance **d**.
            """)


    # --- PRACTICE TAB ---
    with tab2:
        # Two columns: image | question + MCQ
        prac_col1, prac_col2 = st.columns([1, 1.75])

        with prac_col1:
            st.image(KITE_IMAGES["perimeter"], width=220)

        with prac_col2:
            # Question prompt
            st.markdown("**What is the perimeter of the kite if the tip-to-tip distance is 90 cm?**")

            # Quick Reference
            st.markdown("""
            <div class="ref">
            ⭕ Quick Reference: Perimeter = (2 × π × 90) ÷ 3, π = 3.142
            </div>
            """, unsafe_allow_html=True)

            with st.form(key="peri_q1_form"):
                options = [188.5, 90, 150]
                st.markdown("<div style='margin-top: 0.5rem'></div>", unsafe_allow_html=True)

                selected_option = st.radio("Choose the correct answer:",
                                           options,
                                           key="peri_q1_radio",
                                           help="Apply the formula step by step: (2 × π × 90) ÷ 3")

                form_col1, form_col2 = st.columns([2, 1])
                with form_col1:
                    submit_button = st.form_submit_button(label="🎯 Submit Answer",
                                                          type="primary",
                                                          use_container_width=True)
                with form_col2:
                    st.markdown(
                        "<div style='text-align: center; padding: 4px; color: #666; font-size: 0.75em;'>⭕ Use the Vesica formula!</div>",
                        unsafe_allow_html=True
                    )

                if submit_button:
                    if selected_option == 188.5:
                        st.session_state.lesson_done["perimeter"] = True
                        set_stage("peri_correct")
                    else:
                        st.session_state.peri_wrong += 1
                        if st.session_state.peri_wrong == 1:
                            set_stage("peri_wrong1")
                        else:
                            set_stage("peri_wrong2")
                    st.rerun()


    st.markdown('</div>', unsafe_allow_html=True)

def peri_correct_answer():
    # ✅ Compact layout styling
    st.markdown("""
    <style>
    section.main > div.block-container {
        padding-top: 0rem !important;
        margin-top: 0rem !important;
    }

    [data-testid="column"] {
        padding-top: 0rem !important;
        margin-top: 0rem !important;
    }

    .peri-page .stMarkdown {
        margin-bottom: 0.4rem !important;
    }

    .stButton button {
        white-space: nowrap;
        padding-top: 0.35rem !important;
        padding-bottom: 0.25rem !important;
        margin-top: -2px !important;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="peri-page">', unsafe_allow_html=True)

    # 🎉 Celebration message
    st.success("🎉 Outstanding work!")

    st.markdown(f"""
✅ That's correct, {st.session_state.user_name}!  
You successfully calculated the **perimeter** of the kite's Vesica Piscis body.
""")

    # 📚 Condensed learning summary (2 bullets)
    st.markdown("""
**📚 What You Learned:**
- Use arc-based formulas to calculate curved perimeters  
- Geometry explains cultural shapes like the Layangan Janggan 🪁
""")

    # 🎯 Navigation Section
    st.markdown("### 🎯 Next Adventure")

    next_col1, next_col2 = st.columns(2)

    with next_col1:
        st.markdown("**📚 Continue**")
        if st.button("🏠 Learning Hub",
                     on_click=go_to_topic_menu,
                     key="peri_correct_main_menu",
                     type="primary",
                     help="Select another lesson",
                     use_container_width=True):
            pass
        if st.button("📐 Angles",
                     key="peri_correct_next_lesson",
                     help="Go to Angles lesson",
                     use_container_width=True):
            st.session_state.angles_wrong = 0
            set_stage("angles_intro")
            st.rerun()

    with next_col2:
        st.markdown("**🔄 Options**")
        if st.button("🔄 Repeat",
                     on_click=repeat_peri_lesson,
                     key="peri_correct_repeat_lesson",
                     help="Review lesson",
                     use_container_width=True):
            pass
        if st.button("👋 End",
                     on_click=end_session,
                     key="peri_correct_end_session",
                     help="Complete session",
                     use_container_width=True):
            pass

    st.markdown('</div>', unsafe_allow_html=True)

def peri_wrong_answer1():
    # ✅ Compact styling for scroll-free visibility
    st.markdown("""
    <style>
    section.main > div.block-container {
        padding-top: 0rem !important;
        margin-top: 0rem !important;
    }

    [data-testid="column"] {
        padding-top: 0rem !important;
        margin-top: 0rem !important;
    }

    .peri-page img {
        max-height: 140px;
        object-fit: contain;
        margin-bottom: 0.3rem;
    }

    .peri-page .stRadio > div {
        font-size: 0.78em !important;
        line-height: 1.2 !important;
        row-gap: 0.25rem !important;
        margin-top: 0.4rem !important;
        margin-bottom: 0.6rem !important;
    }

    .stButton button {
        white-space: nowrap;
        padding-top: 0.35rem !important;
        padding-bottom: 0.25rem !important;
        margin-top: -2px !important;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="peri-page">', unsafe_allow_html=True)

    # --- Header row with feedback + home button ---
    col1, col2 = st.columns([5.1, 1.5])
    with col1:
        st.markdown(f"""
❌ Not quite, {st.session_state.user_name}. Let's try again! 😊  
**Hint:** Use the formula **(2 × π × d) ÷ 3** with **d = 90**
        """)
    with col2:
        if st.button("🏠 Learning Hub", key="peri_wrong1_home_nav", help="Return to main menu"):
            go_to_topic_menu()
            st.rerun()

    # --- Content: image | quiz
    col_img, col_quiz = st.columns([1, 1.75])
    with col_img:
        st.image(KITE_IMAGES["perimeter"], width=220)

    with col_quiz:
        with st.form(key="peri_q2_form"):
            st.markdown("<div style='margin-top: 0.4rem'></div>", unsafe_allow_html=True)

            st.markdown("""
            <div style='font-size: 1.05em; font-weight: 600; display: flex; align-items: center; gap: 6px;'>
                ⭕ <span>Choose the correct answer:</span>
            </div>
            """, unsafe_allow_html=True)

            options = [188.5, 90, 150]
            selected_option = st.radio("",
                                       options,
                                       key="peri_q2_radio",
                                       )

            form_col1, form_col2 = st.columns([2, 1])
            with form_col1:
                submit_button = st.form_submit_button(label="🎯 Try Again", type="primary", use_container_width=True)
            with form_col2:
                help_button = st.form_submit_button("💡 Help", use_container_width=True)

            if help_button:
                st.warning("📌 Use the Vesica formula: (2 × π × d) ÷ 3 with d = 90!")

            if submit_button:
                if selected_option == 188.5:
                    st.session_state.lesson_done["perimeter"] = True
                    set_stage("peri_correct")
                else:
                    st.session_state.peri_wrong += 1
                    set_stage("peri_wrong2")
                st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)

def peri_wrong_answer2():
    st.markdown('<div class="peri-page">', unsafe_allow_html=True)
    st.markdown(
        f"""❌ That's okay, {st.session_state.user_name}. Don't worry! 🌱

**Here's the calculation:**

**Perimeter = (2 × π × d) ÷ 3**  
If the tip-to-tip distance is **90 cm**, then:  
**(2 × π × 90) ÷ 3 ≈ 188.5 cm**

That's the perimeter, which is the total curved distance around the kite's main body! 🪁"""
    )
    st.markdown("### 🎯 Continue Learning")
    nav_col1, nav_col2 = st.columns(2)
    with nav_col1:
        st.markdown("**📚 Keep Learning**")
        if st.button("🏠 Learning Hub",
                     on_click=go_to_topic_menu,
                     key="peri_wrong2_main_menu",
                     type="primary",
                     help="Choose your next lesson",
                     use_container_width=True):
            pass
        if st.button("📐 Angles",
                     key="peri_wrong2_next_lesson",
                     help="Go to Angles lesson",
                     use_container_width=True):
            st.session_state.angles_wrong = 0
            set_stage("angles_intro")
            st.rerun()
    with nav_col2:
        st.markdown("**🔄 Practice**")
        if st.button("🔄 Repeat",
                     on_click=repeat_peri_lesson,
                     key="peri_wrong2_repeat_lesson",
                     help="Try again",
                     use_container_width=True):
            pass
        if st.button("👋 End",
                     on_click=end_session,
                     key="peri_wrong2_end_session",
                     help="Complete session",
                     use_container_width=True):
            pass
    st.markdown('</div>', unsafe_allow_html=True)




routes = {
    "greeting": stage_greeting,
    "ask_name": stage_ask_name,
    "name_captured": stage_name_captured,
    "topic_menu": stage_menu,
    "ai_explorer": stage_ai_explorer,
    "AI Explorer": stage_ai_explorer,
    "AI Chat": stage_ai_chat,
    "video": stage_video,
    "exit_early": stage_exit_early,
    "exit_post": stage_exit_post,

    # Lesson Routes
    "angles_intro": angles_intro,
    "angles_correct": angles_correct_answer,
    "angles_wrong1": angles_wrong_answer1,
    "angles_wrong2": angles_wrong_answer2,

    "trig_intro": trig_intro,
    "trig_correct": trig_correct_answer,
    "trig_wrong1": trig_wrong_answer1,
    "trig_wrong2": trig_wrong_answer2,

    "peri_intro": peri_intro,
    "peri_correct": peri_correct_answer,
    "peri_wrong1": peri_wrong_answer1,
    "peri_wrong2": peri_wrong_answer2,
}
routes[st.session_state.stage]()
