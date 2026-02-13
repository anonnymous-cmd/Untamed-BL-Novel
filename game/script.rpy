# --- Character Setup ---
define wwx = Character("Wei Wuxian", color="#ff3333") 
define lwj = Character("Lan Wangji", color="#33ccff")

# --- Stats Logic ---
default cultivation_level = 1
default soulmate_bond = 0
default path_chosen = "None"

label start:
    "The year is the Great Era of Cultivation. I, Wei Wuxian, have returned."
    
    show wwx_happy # This expects an image named wwx_happy.png
    wwx "Lan Zhan! If I stay here in Gusu, will you hide me in your Jingshi?"

    menu:
        "Hand him the Emperor's Smile wine":
            $ soulmate_bond += 10
            $ path_chosen = "Rebel"
            lwj "Alcohol is forbidden. But... just this once."
            "Lan Wangji's expression remains cold, but his ears are red."

        "Ask him to play 'Inquiry' for you":
            $ cultivation_level += 5
            $ soulmate_bond += 20
            $ path_chosen = "Cultivator"
            lwj "Sit. I will play for you until dawn."

    "Your bond with Lan Wangji is now [soulmate_bond]."
    "Your path is set to: [path_chosen]."
    
    if soulmate_bond > 15:
        "The ribbon on his forehead is no longer off-limits to you."
        
    return
