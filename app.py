import streamlit as st
import numpy as np
from math import gcd
from Crypto.Cipher import DES

st.set_page_config(
    page_title="🐢 Mã hóa Cổ điển - Rùa Biển",
    page_icon="🐢",
    layout="wide"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@400;600;700&family=Fredoka:wght@500;600;700&display=swap');

.stApp {
    background:
        radial-gradient(ellipse at top, rgba(168, 230, 207, 0.5) 0%, transparent 55%),
        radial-gradient(ellipse at bottom, rgba(38, 139, 147, 0.4) 0%, transparent 60%),
        linear-gradient(180deg,
            #d4f1e8 0%,
            #a8e6cf 20%,
            #7dd3c0 45%,
            #4db6ac 70%,
            #2e8b8f 90%,
            #1a5f6f 100%);
    background-attachment: fixed;
}

.stApp::after {
    content: "🫧 🫧 🫧 🫧 🫧 🫧 🫧 🫧 🫧 🫧 🫧 🫧 🫧 🫧 🫧 🫧 🫧 🫧 🫧 🫧 🫧 🫧 🫧 🫧";
    position: fixed;
    bottom: -10px;
    left: 0;
    right: 0;
    font-size: 26px;
    letter-spacing: 4px;
    opacity: 0.35;
    pointer-events: none;
    z-index: 0;
    text-align: center;
    overflow: hidden;
    white-space: nowrap;
    animation: bubbleFloat 6s ease-in-out infinite;
}

@keyframes bubbleFloat {
    0%, 100% { transform: translateY(0); opacity: 0.3; }
    50%      { transform: translateY(-12px); opacity: 0.55; }
}

html, body, [class*="css"], .stMarkdown, p, label, div {
    font-family: 'Quicksand', 'Comic Sans MS', sans-serif !important;
}

h1 {
    font-family: 'Fredoka', sans-serif !important;
    color: #2e8b57 !important;
    text-align: center !important;
    font-size: 2.9rem !important;
    text-shadow:
        3px 3px 0 #d4f1e8,
        5px 5px 10px rgba(46, 139, 87, 0.35),
        0 0 25px rgba(122, 211, 192, 0.55) !important;
    padding: 15px 0 5px 0 !important;
    letter-spacing: 1px;
}

h2, h3 {
    color: #1a5f6f !important;
    font-weight: 700 !important;
}

.stButton > button {
    background: linear-gradient(135deg, #a8e6cf, #6fcf97, #2e8b57) !important;
    color: #ffffff !important;
    border-radius: 25px !important;
    border: 3px solid #d4f1e8 !important;
    padding: 12px 28px !important;
    font-weight: 700 !important;
    font-size: 1.05rem !important;
    box-shadow:
        0 6px 18px rgba(46, 139, 87, 0.45),
        inset 0 -3px 0 rgba(20, 80, 50, 0.35) !important;
    transition: all 0.3s ease !important;
    width: 100%;
    text-shadow: 1px 1px 2px rgba(0, 50, 30, 0.4);
}
.stButton > button:hover {
    transform: translateY(-3px) scale(1.03) rotate(0.5deg);
    box-shadow:
        0 10px 24px rgba(46, 139, 87, 0.65),
        inset 0 -3px 0 rgba(20, 80, 50, 0.45) !important;
    background: linear-gradient(135deg, #c5f0e0, #7dd3c0, #3ba06a) !important;
}

.stTextArea textarea, .stTextInput input, .stNumberInput input {
    border-radius: 16px !important;
    border: 2.5px solid #7dd3c0 !important;
    background-color: #f0fbf7 !important;
    padding: 12px !important;
    font-size: 1rem !important;
    color: #1a5f6f !important;
    transition: all 0.3s ease !important;
}
.stTextArea textarea:focus, .stTextInput input:focus, .stNumberInput input:focus {
    border-color: #2e8b57 !important;
    background-color: #e8f8f2 !important;
    box-shadow: 0 0 0 4px rgba(168, 230, 207, 0.45) !important;
}

[data-testid="stSidebar"] {
    background:
        linear-gradient(180deg,
            #d4f1e8 0%,
            #a8e6cf 30%,
            #7dd3c0 65%,
            #4db6ac 100%);
    border-right: 3px dashed #2e8b57;
}
[data-testid="stSidebar"] h2 {
    color: #1a5f6f !important;
    font-family: 'Fredoka', sans-serif !important;
    text-shadow: 1px 1px 0 #d4f1e8;
}

.stSelectbox > div > div, .stMultiSelect > div > div {
    border-radius: 16px !important;
    border: 2.5px solid #7dd3c0 !important;
    background-color: #f0fbf7 !important;
}

.stAlert {
    border-radius: 16px !important;
    border-left: 6px solid #2e8b57 !important;
    background-color: #e8f8f2 !important;
}

.streamlit-expanderHeader, [data-testid="stExpander"] {
    border-radius: 16px !important;
    background-color: #f0fbf7 !important;
    border: 2px dashed #7dd3c0 !important;
}

.turtle-bg {
    position: fixed;
    top: -10%;
    font-size: 32px;
    animation: turtleSwim 16s linear infinite;
    opacity: 0.7;
    pointer-events: none;
    z-index: 0;
    filter: drop-shadow(2px 2px 5px rgba(20, 80, 60, 0.25));
}
@keyframes turtleSwim {
    0%   { transform: translateY(-10vh) translateX(0) rotate(-8deg); opacity: 0; }
    10%  { opacity: 0.75; }
    25%  { transform: translateY(25vh) translateX(15px) rotate(5deg); }
    50%  { transform: translateY(50vh) translateX(-10px) rotate(-5deg); }
    75%  { transform: translateY(75vh) translateX(20px) rotate(8deg); }
    90%  { opacity: 0.75; }
    100% { transform: translateY(110vh) translateX(-15px) rotate(-8deg); opacity: 0; }
}
.turtle-bg:nth-child(1)  { left: 3%;  animation-delay: 0s;    font-size: 36px; }
.turtle-bg:nth-child(2)  { left: 16%; animation-delay: 2.5s;  font-size: 26px; }
.turtle-bg:nth-child(3)  { left: 30%; animation-delay: 6s;    font-size: 32px; }
.turtle-bg:nth-child(4)  { left: 44%; animation-delay: 1s;    font-size: 28px; }
.turtle-bg:nth-child(5)  { left: 58%; animation-delay: 8s;    font-size: 38px; }
.turtle-bg:nth-child(6)  { left: 72%; animation-delay: 4s;    font-size: 30px; }
.turtle-bg:nth-child(7)  { left: 85%; animation-delay: 10s;   font-size: 24px; }
.turtle-bg:nth-child(8)  { left: 94%; animation-delay: 5.5s;  font-size: 34px; }

.result-box {
    background:
        radial-gradient(circle at 20% 30%, rgba(168, 230, 207, 0.6) 0%, transparent 40%),
        radial-gradient(circle at 80% 70%, rgba(122, 211, 192, 0.5) 0%, transparent 40%),
        linear-gradient(135deg, #e8f8f2, #d4f1e8, #c5f0e0);
    border: 3px dashed #2e8b57;
    border-radius: 22px;
    padding: 18px 24px;
    margin-top: 15px;
    box-shadow:
        0 6px 18px rgba(46, 139, 87, 0.3),
        inset 0 0 30px rgba(212, 241, 232, 0.6);
    position: relative;
}
.result-box::before {
    content: "🐢";
    position: absolute;
    top: -18px;
    left: 20px;
    font-size: 30px;
    background: #d4f1e8;
    border-radius: 50%;
    padding: 2px 6px;
    box-shadow: 0 3px 8px rgba(0,0,0,0.12);
    animation: bobHead 3s ease-in-out infinite;
}
@keyframes bobHead {
    0%, 100% { transform: translateY(0) rotate(-5deg); }
    50%      { transform: translateY(-3px) rotate(5deg); }
}
.result-box h4 {
    color: #2e8b57 !important;
    margin: 0 0 10px 0 !important;
    font-family: 'Fredoka', sans-serif !important;
    font-size: 1.2rem !important;
}
.result-text {
    color: #1a5f6f;
    font-size: 1.18rem;
    font-weight: 600;
    word-break: break-word;
    line-height: 1.5;
}

.turtle-footer {
    text-align: center;
    color: #1a5f6f;
    padding: 20px 0 30px 0;
    font-size: 0.98rem;
    font-weight: 600;
    text-shadow: 1px 1px 0 rgba(212, 241, 232, 0.9);
}

hr {
    border: none;
    height: 6px;
    background:
        radial-gradient(circle, #2e8b57 30%, transparent 30%),
        radial-gradient(circle, #7dd3c0 30%, transparent 30%);
    background-size: 20px 20px;
    background-position: 0 0, 10px 10px;
    background-repeat: repeat-x;
    margin: 20px 0;
    opacity: 0.65;
}

.stCaption, small {
    color: #1a5f6f !important;
    font-weight: 600 !important;
}

.stRadio label, .stCheckbox label {
    color: #1a5f6f !important;
    font-weight: 600 !important;
}
</style>

<div class="turtle-bg">🐢</div>
<div class="turtle-bg">🐢</div>
<div class="turtle-bg">🐢</div>
<div class="turtle-bg">🐢</div>
<div class="turtle-bg">🐢</div>
<div class="turtle-bg">🐢</div>
<div class="turtle-bg">🐢</div>
<div class="turtle-bg">🐢</div>
""", unsafe_allow_html=True)


Z26 = "abcdefghijklmnopqrstuvwxyz"
Z29 = "aăâbcdđeêghiklmnoôơpqrstuưvxy"

def get_alphabet(use_z29):
    return Z29 if use_z29 else Z26

def char_to_num(c, alphabet):
    idx = alphabet.find(c.lower())
    return idx if idx >= 0 else -1

def num_to_char(num, alphabet):
    n = len(alphabet)
    return alphabet[num % n]

def mod_inverse(a, m):
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    raise ValueError(f"Không có nghịch đảo modulo của {a} theo {m}")

def caesar_encrypt(text, k, alphabet):
    result = ""
    for c in text:
        idx = char_to_num(c, alphabet)
        if idx >= 0:
            new_c = num_to_char(idx + k, alphabet)
            result += new_c.upper() if c.isupper() else new_c
        else:
            result += c
    return result

def caesar_decrypt(text, k, alphabet):
    return caesar_encrypt(text, -k, alphabet)

def substitution_encrypt(text, key, alphabet):
    if len(key) != len(alphabet):
        raise ValueError(f"Khóa phải có đúng {len(alphabet)} ký tự")
    if len(set(key)) != len(key):
        raise ValueError("Khóa không được có ký tự trùng lặp")
    result = ""
    for c in text:
        idx = char_to_num(c, alphabet)
        if idx >= 0:
            new_c = key[idx]
            result += new_c.upper() if c.isupper() else new_c
        else:
            result += c
    return result

def substitution_decrypt(text, key, alphabet):
    result = ""
    for c in text:
        idx = key.find(c.lower())
        if idx >= 0:
            new_c = alphabet[idx]
            result += new_c.upper() if c.isupper() else new_c
        else:
            result += c
    return result

def vigenere_encrypt(text, key, alphabet):
    key_low = key.lower()
    shifts = [alphabet.index(c) for c in key_low if c in alphabet]
    if not shifts:
        raise ValueError("Từ khóa không hợp lệ")
    result = ""
    ki = 0
    for c in text:
        idx = char_to_num(c, alphabet)
        if idx >= 0:
            shift = shifts[ki % len(shifts)]
            new_c = num_to_char(idx + shift, alphabet)
            result += new_c.upper() if c.isupper() else new_c
            ki += 1
        else:
            result += c
    return result

def vigenere_decrypt(text, key, alphabet):
    key_low = key.lower()
    shifts = [alphabet.index(c) for c in key_low if c in alphabet]
    if not shifts:
        raise ValueError("Từ khóa không hợp lệ")
    result = ""
    ki = 0
    for c in text:
        idx = char_to_num(c, alphabet)
        if idx >= 0:
            shift = shifts[ki % len(shifts)]
            new_c = num_to_char(idx - shift, alphabet)
            result += new_c.upper() if c.isupper() else new_c
            ki += 1
        else:
            result += c
    return result

def affine_encrypt(text, a, b, alphabet):
    n = len(alphabet)
    if gcd(a, n) != 1:
        raise ValueError(f"gcd({a}, {n}) phải = 1")
    result = ""
    for c in text:
        idx = char_to_num(c, alphabet)
        if idx >= 0:
            new_c = num_to_char(a * idx + b, alphabet)
            result += new_c.upper() if c.isupper() else new_c
        else:
            result += c
    return result

def affine_decrypt(text, a, b, alphabet):
    n = len(alphabet)
    a_inv = mod_inverse(a, n)
    result = ""
    for c in text:
        idx = char_to_num(c, alphabet)
        if idx >= 0:
            new_c = num_to_char(a_inv * (idx - b), alphabet)
            result += new_c.upper() if c.isupper() else new_c
        else:
            result += c
    return result

def hill_encrypt(text, K, alphabet):
    n = len(alphabet)
    idxs = [char_to_num(c, alphabet) for c in text if char_to_num(c, alphabet) >= 0]
    while len(idxs) % 2 != 0:
        idxs.append(0)
    result = ""
    for i in range(0, len(idxs), 2):
        p1, p2 = idxs[i], idxs[i + 1]
        c1 = (K[0][0] * p1 + K[0][1] * p2) % n
        c2 = (K[1][0] * p1 + K[1][1] * p2) % n
        result += num_to_char(c1, alphabet).upper()
        result += num_to_char(c2, alphabet).upper()
    return result

def hill_decrypt(text, K, alphabet):
    n = len(alphabet)
    det = (K[0][0] * K[1][1] - K[0][1] * K[1][0]) % n
    if gcd(det, n) != 1:
        raise ValueError(f"det(K)={det} phải nguyên tố cùng nhau với {n}")
    det_inv = mod_inverse(det, n)
    Kinv = [
        [(K[1][1] * det_inv) % n, (-K[0][1] * det_inv) % n],
        [(-K[1][0] * det_inv) % n, (K[0][0] * det_inv) % n]
    ]
    idxs = [char_to_num(c, alphabet) for c in text if char_to_num(c, alphabet) >= 0]
    while len(idxs) % 2 != 0:
        idxs.append(0)
    result = ""
    for i in range(0, len(idxs), 2):
        c1, c2 = idxs[i], idxs[i + 1]
        p1 = (Kinv[0][0] * c1 + Kinv[0][1] * c2) % n
        p2 = (Kinv[1][0] * c1 + Kinv[1][1] * c2) % n
        result += num_to_char(p1, alphabet)
        result += num_to_char(p2, alphabet)
    return result

def des_encrypt(text, key):
    try:
        key_bytes = bytes.fromhex(key)
        text_bytes = bytes.fromhex(text)
    except ValueError:
        raise ValueError("Dữ liệu và Khóa phải là chuỗi Hexadecimal hợp lệ!")
    
    if len(key_bytes) != 8:
        raise ValueError("Khóa DES phải dài đúng 8 bytes (16 ký tự Hex).")
    if len(text_bytes) != 8:
        raise ValueError("Bản rõ DES (1 khối) phải dài đúng 8 bytes (16 ký tự Hex).")
        
    cipher = DES.new(key_bytes, DES.MODE_ECB)
    encrypted = cipher.encrypt(text_bytes)
    return encrypted.hex().upper()

def des_decrypt(text, key):
    try:
        key_bytes = bytes.fromhex(key)
        text_bytes = bytes.fromhex(text)
    except ValueError:
        raise ValueError("Dữ liệu và Khóa phải là chuỗi Hexadecimal hợp lệ!")
        
    if len(key_bytes) != 8:
        raise ValueError("Khóa DES phải dài đúng 8 bytes (16 ký tự Hex).")
    if len(text_bytes) != 8:
        raise ValueError("Bản mã DES (1 khối) phải dài đúng 8 bytes (16 ký tự Hex).")
        
    cipher = DES.new(key_bytes, DES.MODE_ECB)
    decrypted = cipher.decrypt(text_bytes)
    return decrypted.hex().upper()


st.title("🐢 Ứng dụng Mã hóa Cổ điển 🐢")
st.markdown(
    "<p style='text-align:center; color:#1a5f6f; font-size:1.15rem; font-weight:600; "
    "text-shadow:1px 1px 0 rgba(212,241,232,0.9);'>"
    "🌊 Dịch vòng • Thay thế • Vigenere • Affine • Hill • DES 🌊<br>"
    "<span style='font-size:0.98rem;'>Trên hệ Z26 (tiếng Anh), Z29 (tiếng Việt) và Hexadecimal (DES)</span>"
    "</p>",
    unsafe_allow_html=True
)
st.markdown("---")

with st.sidebar:
    st.header("🐢 Cấu hình")

    cipher_type = st.selectbox(
        "🌿 Loại mã hóa:",
        [
            "Dịch vòng (Caesar)",
            "Thay thế (Substitution)",
            "Vigenere",
            "Affine",
            "Hill (2x2)",
            "DES (Hexadecimal)"
        ]
    )

    if cipher_type == "DES (Hexadecimal)":
        st.info("🔐 DES yêu cầu đầu vào là chuỗi Hexadecimal (16 ký tự cho 1 khối 64-bit).")
        system_type = "DES (Hexadecimal)"
        use_z29 = False
        alphabet = ""
        n = 0
    else:
        system_type = st.radio(
            "🌊 Hệ mã hóa:",
            ["Z26 - Tiếng Anh 🇬🇧", "Z29 - Tiếng Việt 🇻🇳"]
        )
        use_z29 = system_type.startswith("Z29")
        alphabet = get_alphabet(use_z29)
        n = len(alphabet)
        st.info(f"📖 Bảng chữ cái ({n} ký tự):\n`{alphabet}`")

    st.markdown("### 🔑 Khóa")

    if cipher_type == "Dịch vòng (Caesar)":
        key_input = st.number_input("Số dịch chuyển k:", min_value=0, max_value=n - 1, value=3)
        st.caption(f"Nhập số nguyên từ 0 đến {n-1}")

    elif cipher_type == "Thay thế (Substitution)":
        default_sub = "qwertyuiopasdfghjklzxcvbnm"
        if use_z29:
            default_sub = "aăâbcdđeêghiklmnoôơpqrstuưvxy"[::-1]
        key_input = st.text_input(
            f"Bảng thay thế ({n} ký tự):",
            value=default_sub[:n] if len(default_sub) >= n else default_sub
        )
        st.caption(f"Phải có đúng {n} ký tự, không trùng lặp")

    elif cipher_type == "Vigenere":
        key_input = st.text_input("Từ khóa:", value="TURTLE")
        st.caption("Ví dụ: TURTLE, OCEAN, KEY")

    elif cipher_type == "Affine":
        col1, col2 = st.columns(2)
        with col1:
            a_val = st.number_input("Hệ số a:", min_value=1, max_value=n - 1, value=5)
        with col2:
            b_val = st.number_input("Hệ số b:", min_value=0, max_value=n - 1, value=8)
        key_input = (int(a_val), int(b_val))
        if gcd(a_val, n) != 1:
            st.error(f"⚠️ gcd({a_val}, {n}) = {gcd(a_val, n)} ≠ 1. Không hợp lệ!")

    elif cipher_type == "Hill (2x2)":
        st.markdown("Nhập ma trận K = [[a, b], [c, d]]:")
        c1, c2 = st.columns(2)
        with c1:
            a_val = st.number_input("a:", min_value=0, max_value=n - 1, value=3, key="hill_a")
            cc_val = st.number_input("c:", min_value=0, max_value=n - 1, value=2, key="hill_c")
        with c2:
            b_val = st.number_input("b:", min_value=0, max_value=n - 1, value=3, key="hill_b")
            d_val = st.number_input("d:", min_value=0, max_value=n - 1, value=5, key="hill_d")
        key_input = [[int(a_val), int(b_val)], [int(cc_val), int(d_val)]]
        det = (a_val * d_val - b_val * cc_val) % n
        if gcd(det, n) != 1:
            st.error(f"⚠️ det(K)={det}, gcd({det}, {n})≠1. Không khả nghịch!")
        else:
            st.success(f"✅ det(K) = {det}. Khóa hợp lệ!")

    elif cipher_type == "DES (Hexadecimal)":
        key_input = st.text_input(
            "Khóa DES (16 ký tự Hex):", 
            value="AABB09182736CCDD",
            max_chars=16
        )
        if len(key_input) != 16:
            st.error("⚠️ Khóa DES phải có đúng 16 ký tự Hexadecimal (64 bit)!")
        elif not all(c in "0123456789ABCDEFabcdef" for c in key_input):
            st.error("⚠️ Khóa chỉ được chứa các ký tự 0-9, A-F!")
        else:
            st.success("✅ Khóa hợp lệ!")


def process(text, encrypt):
    if cipher_type == "DES (Hexadecimal)":
        return des_encrypt(text, key_input) if encrypt else des_decrypt(text, key_input)
        
    elif cipher_type == "Dịch vòng (Caesar)":
        k = int(key_input)
        return caesar_encrypt(text, k, alphabet) if encrypt else caesar_decrypt(text, k, alphabet)
        
    elif cipher_type == "Thay thế (Substitution)":
        key = key_input.lower().strip()
        return substitution_encrypt(text, key, alphabet) if encrypt else substitution_decrypt(text, key, alphabet)
        
    elif cipher_type == "Vigenere":
        return vigenere_encrypt(text, key_input, alphabet) if encrypt else vigenere_decrypt(text, key_input, alphabet)
        
    elif cipher_type == "Affine":
        a, b = key_input
        return affine_encrypt(text, a, b, alphabet) if encrypt else affine_decrypt(text, a, b, alphabet)
        
    elif cipher_type == "Hill (2x2)":
        return hill_encrypt(text, key_input, alphabet) if encrypt else hill_decrypt(text, key_input, alphabet)
        
    return ""


col_left, col_right = st.columns(2)

if cipher_type == "DES (Hexadecimal)":
    plain_placeholder = "Ví dụ: 123456ABCD132536"
    cipher_placeholder = "Ví dụ: 82DC3A3D3838A1F3"
    plain_label = "Nhập bản rõ Hex (16 ký tự):"
    cipher_label = "Nhập bản mã Hex (16 ký tự):"
else:
    plain_placeholder = "Ví dụ: turtle swims slowly 🐢"
    cipher_placeholder = "Ví dụ: wxuvsn dlaqj rwlyqn 🌊"
    plain_label = "Nhập văn bản cần mã hóa:"
    cipher_label = "Nhập văn bản cần giải mã:"

with col_left:
    st.subheader("📝 Bản rõ")
    plain_text = st.text_area(
        plain_label,
        height=200,
        key="plain",
        placeholder=plain_placeholder
    )

with col_right:
    st.subheader("🔒 Bản mã")
    cipher_text = st.text_area(
        cipher_label,
        height=200,
        key="cipher",
        placeholder=cipher_placeholder
    )

st.markdown("---")

btn_col1, btn_col2, btn_col3 = st.columns(3)

with btn_col1:
    encrypt_btn = st.button("🔒 Mã hóa 🐢", use_container_width=True, type="primary")

with btn_col2:
    decrypt_btn = st.button("🔓 Giải mã 🌊", use_container_width=True)

with btn_col3:
    clear_btn = st.button("🗑️ Xóa tất cả 🧹", use_container_width=True)


if encrypt_btn:
    if not plain_text.strip():
        st.warning("🐢 Vui lòng nhập bản rõ nhé!")
    else:
        try:
            result = process(plain_text, encrypt=True)
            st.success("🐢 Mã hóa thành công! 🌊")
            st.markdown(f"""
            <div class="result-box">
                <h4>📤 Kết quả (Bản mã)</h4>
                <div class="result-text">{result}</div>
            </div>
            """, unsafe_allow_html=True)
            with st.expander("ℹ️ Chi tiết"):
                st.write(f"- Loại mã hóa: **{cipher_type}**")
                st.write(f"- Hệ mã hóa: **{system_type}**")
                st.write(f"- Khóa: **{key_input}**")
                st.write(f"- Bản rõ: `{plain_text}`")
                st.write(f"- Bản mã: `{result}`")
        except Exception as e:
            st.error(f"😢 Lỗi: {e}")

if decrypt_btn:
    if not cipher_text.strip():
        st.warning("🐢 Vui lòng nhập bản mã nhé!")
    else:
        try:
            result = process(cipher_text, encrypt=False)
            st.success("🐢 Giải mã thành công! 🌊")
            st.markdown(f"""
            <div class="result-box">
                <h4>📤 Kết quả (Bản rõ)</h4>
                <div class="result-text">{result}</div>
            </div>
            """, unsafe_allow_html=True)
            with st.expander("ℹ️ Chi tiết"):
                st.write(f"- Loại mã hóa: **{cipher_type}**")
                st.write(f"- Hệ mã hóa: **{system_type}**")
                st.write(f"- Khóa: **{key_input}**")
                st.write(f"- Bản mã: `{cipher_text}`")
                st.write(f"- Bản rõ: `{result}`")
        except Exception as e:
            st.error(f"😢 Lỗi: {e}")

if clear_btn:
    st.rerun()


st.markdown("---")
with st.expander("📚 Hướng dẫn sử dụng chi tiết"):
    st.markdown("""
    ### 🐢 Định dạng khóa cho từng loại mã hóa

    | Loại mã hóa | Khóa | Ví dụ |
    |---|---|---|
    | **Dịch vòng** | Số nguyên k | `3` |
    | **Thay thế** | Bảng chữ cái đủ 26/29 ký tự | `qwertyuiopasdfghjklzxcvbnm` |
    | **Vigenere** | Từ khóa chữ | `TURTLE` |
    | **Affine** | Cặp (a, b), gcd(a,n)=1 | `a=5, b=8` |
    | **Hill 2×2** | Ma trận a,b,c,d | `a=3, b=3, c=2, d=5` |
    | **DES** | Chuỗi 16 ký tự Hex (64-bit) | `AABB09182736CCDD` |

    ### 🌊 Ví dụ kiểm thử

    - **Caesar Z26:** `hello world`, k=3 → `khoor zruog`
    - **Vigenere Z26:** `ATTACKATDAWN`, key=`LEMON` → `LXFOPVEFRNHR`
    - **Affine Z26:** `affine cipher`, a=5,b=8 → `ihhwvc swfrcp`
    - **Hill 2x2 Z26:** `help`, K=[[3,3],[2,5]] → `HIAT`
    - **Caesar Z29:** `xin chào`, k=3 → dịch chuyển trên bảng 29 ký tự tiếng Việt
    - **DES (Hex):** Bản rõ: `123456ABCD132536`, Khóa: `AABB09182736CCDD` → Kết quả: `82DC3A3D3838A1F3`
    """)

st.markdown(
    "<div class='turtle-footer'>"
    "🐢 Made with <b>Streamlit</b> + <b>Python</b> 🐢<br>"
    "🌊 Chậm mà chắc — như rùa biển! 🐢"
    "</div>",
    unsafe_allow_html=True
)