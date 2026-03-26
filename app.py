import streamlit as st
import pandas as pd
from datetime import datetime

# ページ設定
st.set_page_config(
    page_title="内井祐作 - キャリアポートフォリオ",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# カスタムCSS
st.markdown("""
    <style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .section-header {
        font-size: 2rem;
        font-weight: bold;
        color: #2c3e50;
        border-bottom: 3px solid #1f77b4;
        padding-bottom: 0.5rem;
        margin-top: 2rem;
        margin-bottom: 1rem;
    }
    .skill-badge {
        display: inline-block;
        padding: 0.5rem 1rem;
        margin: 0.25rem;
        background-color: #1f77b4;
        color: white;
        border-radius: 20px;
        font-size: 0.9rem;
    }
    .timeline-item {
        border-left: 3px solid #1f77b4;
        padding-left: 1.5rem;
        margin-bottom: 2rem;
        position: relative;
    }
    .timeline-item::before {
        content: '';
        position: absolute;
        left: -8px;
        top: 0;
        width: 13px;
        height: 13px;
        border-radius: 50%;
        background-color: #1f77b4;
    }
    </style>
    """, unsafe_allow_html=True)

# メインヘッダー
st.markdown('<div class="main-header">📊 内井祐作 - キャリアポートフォリオ</div>', unsafe_allow_html=True)

# サイドバー
with st.sidebar:
    st.image("https://via.placeholder.com/150", caption="プロフィール写真")
    st.markdown("### 📧 連絡先")
    st.markdown("Email: recruit.y.uchii@gmail.com")
    st.markdown("GitHub: [@yusaku-uchii](https://github.com/yusaku-uchii)")
    st.markdown("Qiita: [My Profile](https://qiita.com/ponkomarujp)")
    st.markdown("Note: [My Profile](https://note.com/yusakudata)")

    st.markdown("---")
    st.markdown("### 📍 ナビゲーション")
    selected_section = st.radio(
        "セクション選択",
        ["プロフィール", "スキル", "職務経歴", "プロジェクト", "資格・学歴"]
    )

# プロフィールセクション
if selected_section == "プロフィール":
    st.markdown('<div class="section-header">🙋 プロフィール</div>', unsafe_allow_html=True)

    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown("""
        ### 自己紹介

        データエンジニアとして、データ基盤の構築〜運用まで幅広く携わっています。
        特にSnowflakeのDWH構築の経験に長けています。
        データパイプラインの運用でAWS(Lambda,Glue,S3,Stepfunctions)の経験があります。

        #### 専門分野
        - データエンジニアリング
        """)

    with col2:
        st.markdown("### 📊 基本情報")
        st.info("""
        **経験年数:** 3年9ヶ月+

        **現職:** データエンジニア

        **所在地:** 東京,千葉

        **言語:** 日本語
        """)

# スキルセクション
elif selected_section == "スキル":
    st.markdown('<div class="section-header">💻 スキル</div>', unsafe_allow_html=True)

    tab1, tab2, tab3, tab4 = st.tabs(["プログラミング言語", "クラウド & インフラ", "データベース", "ツール & その他"])

    with tab1:
        st.markdown("### プログラミング言語")
        skills = {
            "Python": 80,
            "SQL": 85,
            "Shell Script": 70
        }

        for skill, level in skills.items():
            st.markdown(f"**{skill}**")
            st.progress(level / 100)

    with tab2:
        st.markdown("### クラウド & インフラ")
        st.markdown("""
        <div>
            <span class="skill-badge">AWS (S3, Lambda, Glue, Stepfunctions)</span>
        </div>
        """, unsafe_allow_html=True)

    with tab3:
        st.markdown("### データベース")
        st.markdown("""
        <div>
            <span class="skill-badge">Snowflake</span>
        </div>
        """, unsafe_allow_html=True)

    with tab4:
        st.markdown("### ツール & その他")
        st.markdown("""
        <div>
            <span class="skill-badge">Git</span>
            <span class="skill-badge">Tableau</span>
            <span class="skill-badge">PowerBI</span>
            <span class="skill-badge">Streamlit</span>
            <span class="skill-badge">Pandas</span>
        </div>
        """, unsafe_allow_html=True)

# 職務経歴セクション
elif selected_section == "職務経歴":
    st.markdown('<div class="section-header">💼 職務経歴</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="timeline-item">
        <h3>土木技師 | 某市役所職員</h3>
        <p><strong>2020年4月 - 2022年9月</strong></p>
        <ul>
            <li>水道本管の工事の発注業務</li>
            <li>市民の窓口業務</li>
        </ul>
    </div>

    <div class="timeline-item">
        <h3>データエンジニア | 株式会社ラクスパートナーズ</h3>
        <p><strong>2022年10月 - 現在</strong></p>
        <ul>
            <li>機械学習エンジニアとして入社</li>
            <li>3ヶ月の研修を経て、実務で活躍</li>
            <li>主にSnowflakeを活用したデータ基盤構築を得意としている</li>

        </ul>
    </div>
    """, unsafe_allow_html=True)

# プロジェクトセクション
elif selected_section == "プロジェクト":
    st.markdown('<div class="section-header">🚀 主要プロジェクト</div>', unsafe_allow_html=True)

    projects = [
        {
            "title": "電気自動車のバッテリー開発における試験データの分析基盤構築",
            "period": "2023年5月 - 2024年6月<",
            "description": "試験データの結果をExcelではなく、PowerBIで可視化",
            "work": [
                "データウェアハウスの設計における要件定義",
                "情報システム部とのセキュリティ要件の折衝",
                "エンドユーザーとの要件定義、プロトタイプ開発",
                ],
            "tech": ["Snowflake","Tableau"],
            "achievements": [
                "初現場ながら、一人で参画し、BI画面のプロトタイプ開発まで実施"
            ]
        },
        {
            "title": "データコンサルティング会社にて商社のデータ基盤構築",
            "period": "2024年7月 - 2025年5月<",
            "description": "OracleDWHからSnowflakeに完全リプレイス業務",
            "work": [
                "データウェアハウスの設計・構築(Snowflake)",
                "SQLを用いたデータ抽出・加工",
                "BIダッシュボードの作成(Tableau)",
                ],
            "tech": ["Snowflake","Tableau"],
            "achievements": [
                "Tableau画面開発担当",
                "ウェアハウスサイズを削減することによる提案で月間30%コスト減",
                "派遣メンバーの業務リード"
            ]
        },
        {
            "title": "人材会社の人事データ分析基盤構築",
            "period": "2025年6月 - 2026年5月",
            "description": "経営層向けの経営報告BI開発におけるデータ基盤構築",
            "work": [
                "データウェアハウスの設計・構築(Snowflake)",
                "SQLを用いたデータ抽出・加工",
                "顧客折衝（要件定義含む）",
                ],
            "tech": ["Python","Lambda","Glue","S3","Stepfunction","CloudWatch","Snowflake","PowerBI"],
            "achievements": [
                "一部運用作業の80%削減を実現",
                "メンバーながら、AIエージェントのチーム内浸透に貢献"
            ]
        }
    ]

    for project in projects:
        with st.expander(f"📦 {project['title']}", expanded=True):
            st.markdown(f"**期間:** {project['period']}")
            st.markdown(f"**概要:** {project['description']}")

            st.markdown("**使用技術:**")
            tech_badges = "".join([f'<span class="skill-badge">{tech}</span>' for tech in project['tech']])
            st.markdown(tech_badges, unsafe_allow_html=True)

            st.markdown("**主な成果:**")
            for achievement in project['achievements']:
                st.markdown(f"- ✅ {achievement}")

# 資格・学歴セクション
elif selected_section == "資格・学歴":
    st.markdown('<div class="section-header">🎓 資格・学歴</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 📜 資格")
        certifications = [
            {"name": "SnowProCore", "date": "2025年3月"},
            {"name": "AWS認定ソリューションアーキテクト - アソシエイト", "date": "2024年11月"},
            {"name": "Python3エンジニア認定データ分析試験", "date": "2022年11月"}
        ]

        for cert in certifications:
            st.markdown(f"""
            <div style="padding: 1rem; margin: 0.5rem 0; background-color: #f0f2f6; border-radius: 5px; border-left: 4px solid #667eea;">
                <strong style="color: #2c3e50;">{cert['name']}</strong><br>
                <small style="color: #5a6c7d;">取得: {cert['date']}</small>
            </div>
            """, unsafe_allow_html=True)

    with col2:
        st.markdown("### 🎓 学歴")
        education = [
            {"school": "日本大学", "major": "生産工学部 土木工学科", "period": "2016年 - 2020年"}
        ]

        for edu in education:
            st.markdown(f"""
            <div style="padding: 1rem; margin: 0.5rem 0; background-color: #f0f2f6; border-radius: 5px; border-left: 4px solid #667eea;">
                <strong style="color: #2c3e50;">{edu['school']}</strong><br>
                <span style="color: #2c3e50;">{edu['major']}</span><br>
                <small style="color: #5a6c7d;">{edu['period']}</small>
            </div>
            """, unsafe_allow_html=True)

# フッター
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #7f8c8d; padding: 2rem;">
    <p>© 2025 内井祐作 - キャリアポートフォリオ</p>
    <p>Built with ❤️ using Streamlit</p>
</div>
""", unsafe_allow_html=True)
