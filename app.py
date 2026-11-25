
import streamlit as st
import pandas as pd

# ==========================================
# 1. CẤU HÌNH TRANG
# ==========================================

st.set_page_config(
    page_title="Movie Review",
    page_icon="🎬",
    layout="wide"
)

# ==========================================
# 2. THIẾT KẾ GIAO DIỆN
# ==========================================

st.markdown("""
<style>
.stApp {
    background-color: #101014;
    color: white;
}

h1, h2, h3 {
    color: #F5C518 !important;
}

.movie-title {
    color: #F5C518;
    font-size: 25px;
    font-weight: bold;
}

div.stButton > button {
    background-color: #F5C518;
    color: black;
    border-radius: 8px;
    font-weight: bold;
    border: none;
}

div.stButton > button:hover {
    background-color: #D9A900;
    color: black;
}

[data-testid="stSidebar"] {
    background-color: #1E1E26;
}
</style>
""", unsafe_allow_html=True)

# ==========================================
# 3. DỮ LIỆU PHIM
# ==========================================

movies = [
    {
        "name": "Interstellar",
        "genre": "Khoa học viễn tưởng",
        "year": 2014,
        "director": "Christopher Nolan",
        "rating": 8.7,
        "duration": "169 phút",
        "description": "Một nhóm phi hành gia thực hiện chuyến du hành xuyên không gian để tìm kiếm hành tinh mới cho nhân loại.",
        "poster": "https://image.tmdb.org/t/p/w500/gEU2QniE6E77NI6lCU6MxlNBvIx.jpg"
    },
    {
        "name": "Inception",
        "genre": "Hành động",
        "year": 2010,
        "director": "Christopher Nolan",
        "rating": 8.8,
        "duration": "148 phút",
        "description": "Dom Cobb là chuyên gia đánh cắp bí mật thông qua những giấc mơ. Anh nhận nhiệm vụ cấy một ý tưởng vào tiềm thức người khác.",
        "poster": "https://image.tmdb.org/t/p/w500/oYuLEt3zVCKq57qu2F8dT7NIa6f.jpg"
    },
    {
        "name": "The Dark Knight",
        "genre": "Hành động",
        "year": 2008,
        "director": "Christopher Nolan",
        "rating": 9.0,
        "duration": "152 phút",
        "description": "Batman phải đối mặt với Joker, tên tội phạm nguy hiểm đang gieo rắc hỗn loạn tại thành phố Gotham.",
        "poster": "https://image.tmdb.org/t/p/w500/qJ2tW6WMUDux911r6m7haRef0WH.jpg"
    },
    {
        "name": "Titanic",
        "genre": "Tình cảm",
        "year": 1997,
        "director": "James Cameron",
        "rating": 7.9,
        "duration": "195 phút",
        "description": "Câu chuyện tình yêu giữa Jack và Rose trên chuyến tàu Titanic huyền thoại.",
        "poster": "https://image.tmdb.org/t/p/w500/9xjZS2rlVxm8SFx8kPC3aIGCOYQ.jpg"
    },
    {
        "name": "Avatar",
        "genre": "Khoa học viễn tưởng",
        "year": 2009,
        "director": "James Cameron",
        "rating": 7.9,
        "duration": "162 phút",
        "description": "Jake Sully đến hành tinh Pandora và dần hòa nhập với người Na'vi, nơi anh phải lựa chọn giữa hai thế giới.",
        "poster": "https://image.tmdb.org/t/p/w500/kyeqWdyUXW608qlYkRqosgbbJyK.jpg"
    },
    {
        "name": "Parasite",
        "genre": "Tâm lý",
        "year": 2019,
        "director": "Bong Joon-ho",
        "rating": 8.5,
        "duration": "132 phút",
        "description": "Một gia đình nghèo tìm cách bước chân vào cuộc sống của một gia đình giàu có, dẫn đến những tình huống bất ngờ.",
        "poster": "https://image.tmdb.org/t/p/w500/7IiTTgloJzvGI1TAYymCfbfl3vT.jpg"
    }
]

# ==========================================
# 4. KHỞI TẠO DỮ LIỆU PHIÊN LÀM VIỆC
# ==========================================

if "reviews" not in st.session_state:
    st.session_state.reviews = []

if "selected_movie" not in st.session_state:
    st.session_state.selected_movie = None

# ==========================================
# 5. MENU ĐIỀU HƯỚNG
# ==========================================

st.sidebar.title("🎬 MOVIE REVIEW")
st.sidebar.markdown("---")

menu = st.sidebar.radio(
    "MENU",
    [
        "🏠 Trang chủ",
        "🎥 Danh sách phim",
        "⭐ Đánh giá phim",
        "📊 Thống kê"
    ]
)

st.sidebar.markdown("---")
st.sidebar.info(
    "Khám phá điện ảnh và chia sẻ cảm nhận của bạn!"
)

# ==========================================
# 6. TRANG CHỦ
# ==========================================

if menu == "🏠 Trang chủ":

    st.title("🎬 MOVIE REVIEW")
    st.subheader("Khám phá thế giới điện ảnh")

    st.write(
        "Chào mừng bạn đến với Movie Review! "
        "Đây là nơi khám phá những bộ phim hấp dẫn, "
        "xem thông tin và chia sẻ đánh giá của riêng bạn."
    )

    st.markdown("---")

    col1, col2, col3 = st.columns(3)

    average_rating = sum(
        movie["rating"] for movie in movies
    ) / len(movies)

    col1.metric("🎥 Tổng số phim", len(movies))
    col2.metric("⭐ Điểm IMDb trung bình", round(average_rating, 1))
    col3.metric("💬 Lượt đánh giá", len(st.session_state.reviews))

    st.markdown("---")

    st.header("🔥 PHIM NỔI BẬT")

    cols = st.columns(3)

    for i, movie in enumerate(movies[:3]):

        with cols[i]:

            st.image(
                movie["poster"],
                use_container_width=True
            )

            st.subheader(movie["name"])

            st.write(f"⭐ IMDb: {movie['rating']}/10")
            st.write(f"📅 Năm: {movie['year']}")
            st.write(f"🎭 {movie['genre']}")

# ==========================================
# 7. DANH SÁCH PHIM
# ==========================================

elif menu == "🎥 Danh sách phim":

    st.title("🎥 DANH SÁCH PHIM")

    search = st.text_input(
        "🔍 Tìm kiếm phim",
        placeholder="Nhập tên phim..."
    )

    genres = ["Tất cả"] + sorted(
        set(movie["genre"] for movie in movies)
    )

    selected_genre = st.selectbox(
        "Lọc theo thể loại",
        genres
    )

    filtered_movies = movies

    if search:
        filtered_movies = [
            movie for movie in filtered_movies
            if search.lower() in movie["name"].lower()
        ]

    if selected_genre != "Tất cả":
        filtered_movies = [
            movie for movie in filtered_movies
            if movie["genre"] == selected_genre
        ]

    st.markdown("---")

    if len(filtered_movies) == 0:

        st.warning("Không tìm thấy bộ phim phù hợp!")

    else:

        for movie in filtered_movies:

            col1, col2 = st.columns([1, 2])

            with col1:

                st.image(
                    movie["poster"],
                    use_container_width=True
                )

            with col2:

                st.subheader(movie["name"])

                st.write(f"⭐ IMDb: {movie['rating']}/10")
                st.write(f"📅 Năm phát hành: {movie['year']}")
                st.write(f"🎭 Thể loại: {movie['genre']}")
                st.write(f"🎬 Đạo diễn: {movie['director']}")
                st.write(f"⏱️ Thời lượng: {movie['duration']}")

                st.write(movie["description"])

                if st.button(
                    f"⭐ Đánh giá {movie['name']}",
                    key=f"rate_{movie['name']}"
                ):

                    st.session_state.selected_movie = movie["name"]

                    st.session_state.go_to_review = True

                    st.rerun()

            st.markdown("---")

# ==========================================
# 8. ĐÁNH GIÁ PHIM
# ==========================================

elif menu == "⭐ Đánh giá phim":

    st.title("⭐ ĐÁNH GIÁ PHIM")

    movie_names = [
        movie["name"] for movie in movies
    ]

    selected_movie = st.session_state.selected_movie

    if selected_movie not in movie_names:
        selected_movie = movie_names[0]

    default_index = movie_names.index(selected_movie)

    selected_movie = st.selectbox(
        "Chọn bộ phim bạn muốn đánh giá",
        movie_names,
        index=default_index
    )

    movie = next(
        movie for movie in movies
        if movie["name"] == selected_movie
    )

    st.markdown("---")

    col1, col2 = st.columns([1, 2])

    with col1:

        st.image(
            movie["poster"],
            use_container_width=True
        )

    with col2:

        st.subheader(movie["name"])

        st.write(f"🎭 Thể loại: {movie['genre']}")
        st.write(f"📅 Năm phát hành: {movie['year']}")
        st.write(f"🎬 Đạo diễn: {movie['director']}")
        st.write(f"⭐ IMDb: {movie['rating']}/10")

        st.write(movie["description"])

    st.markdown("---")

    st.subheader("✍️ CHIA SẺ CẢM NHẬN CỦA BẠN")

    reviewer = st.text_input(
        "Tên người đánh giá",
        placeholder="Nhập tên của bạn..."
    )

    score = st.slider(
        "Điểm đánh giá",
        min_value=1,
        max_value=10,
        value=8
    )

    comment = st.text_area(
        "Nhận xét về bộ phim",
        placeholder="Hãy chia sẻ cảm nhận của bạn về nội dung, diễn xuất, hình ảnh...",
        height=150
    )

    if st.button(
        "📩 GỬI ĐÁNH GIÁ",
        use_container_width=True
    ):

        if reviewer.strip() == "" or comment.strip() == "":

            st.warning(
                "Vui lòng nhập tên và nội dung đánh giá!"
            )

        else:

            st.session_state.reviews.append({
                "reviewer": reviewer,
                "movie": selected_movie,
                "score": score,
                "comment": comment
            })

            st.success(
                "Đánh giá của bạn đã được ghi nhận!"
            )

            st.rerun()

    st.markdown("---")

    st.subheader("💬 CÁC ĐÁNH GIÁ GẦN ĐÂY")

    movie_reviews = [
        review for review in st.session_state.reviews
        if review["movie"] == selected_movie
    ]

    if movie_reviews:

        for review in reversed(movie_reviews):

            with st.container(border=True):

                st.write(f"👤 **{review['reviewer']}**")

                st.write(
                    f"⭐ Điểm đánh giá: {review['score']}/10"
                )

                st.write(review["comment"])

    else:

        st.info(
            "Chưa có đánh giá nào cho bộ phim này."
        )

# ==========================================
# 9. THỐNG KÊ
# ==========================================

elif menu == "📊 Thống kê":

    st.title("📊 THỐNG KÊ ĐÁNH GIÁ")

    if len(st.session_state.reviews) > 0:

        df = pd.DataFrame(
            st.session_state.reviews
        )

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Tổng lượt review",
            len(df)
        )

        col2.metric(
            "Điểm trung bình",
            round(df["score"].mean(), 2)
        )

        col3.metric(
            "Số phim được đánh giá",
            df["movie"].nunique()
        )

        st.markdown("---")

        st.subheader("⭐ ĐIỂM ĐÁNH GIÁ THEO PHIM")

        chart_data = (
            df.groupby("movie")["score"]
            .mean()
            .sort_values(ascending=False)
        )

        st.bar_chart(chart_data)

        st.markdown("---")

        st.subheader("📋 CHI TIẾT ĐÁNH GIÁ")

        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True
        )

        csv_data = df.to_csv(
            index=False
        ).encode("utf-8-sig")

        st.download_button(
            label="📥 TẢI DỮ LIỆU ĐÁNH GIÁ CSV",
            data=csv_data,
            file_name="movie_reviews.csv",
            mime="text/csv"
        )

    else:

        st.info(
            "Chưa có dữ liệu đánh giá để thống kê."
        )

# ==========================================
# 10. CHÂN TRANG
# ==========================================

st.markdown("---")

st.markdown(
    """
    <div style="text-align:center; color:gray;">
        🎬 MOVIE REVIEW <br>
        Discover - Watch - Review <br>
        © 2026 Movie Review
    </div>
    """,
    unsafe_allow_html=True
)
