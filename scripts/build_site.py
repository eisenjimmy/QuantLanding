#!/usr/bin/env python3
"""Build the Quantactic static marketing and legal site.

The content dictionaries in this file are the source of truth. Generated HTML
must never be edited directly; run ``python3 scripts/build_site.py`` after a
content change.
"""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
APP_STORE_URL = "https://apps.apple.com/app/id6795746505"
SUPPORT_EMAIL = "xjimmypark@gmail.com"
LEGAL_EFFECTIVE = "August 9, 2026"

LANGS = [
    {"code": "en", "html_lang": "en", "label": "English", "short": "EN"},
    {"code": "es", "html_lang": "es", "label": "Español", "short": "ES"},
    {"code": "ja", "html_lang": "ja", "label": "日本語", "short": "JA"},
    {"code": "ko", "html_lang": "ko", "label": "한국어", "short": "KO"},
    {"code": "zh-Hans", "html_lang": "zh-Hans", "label": "简体中文", "short": "中文"},
]

# Every user-facing marketing key is explicit per locale. Prices and URLs are
# shared constants because they are data, not translatable prose.
CONTENT = {
    "en": {
        "brand": "Quantactic", "nav_product": "Product", "nav_privacy": "Privacy", "nav_terms": "Terms", "lang_label": "Language",
        "title_index": "Quantactic — Stock Signals, Forecasts & Market Intelligence",
        "meta_index": "Quantactic helps you see what changed, understand unusual market moves, explore probabilistic 7-, 30-, and 90-day outlooks, and review how previous forecasts performed.",
        "title_privacy": "Privacy Policy — Quantactic", "meta_privacy": "Quantactic Privacy Policy",
        "title_terms": "Terms of Use — Quantactic", "meta_terms": "Quantactic Terms of Use",
        "hero_eyebrow": "MARKET INTELLIGENCE THAT SHOWS ITS WORK",
        "hero_h1_1": "See what changed.", "hero_h1_2": "Understand the move.", "hero_h1_3": "Explore what comes next.",
        "hero_lede": "Quantactic turns market activity, explainable signals, probabilistic outlooks, model evidence, comparisons, macro context, and private on-device AI into one focused research workflow.",
        "cta_download": "Download on the App Store", "cta_explore": "Explore Quantactic ↓",
        "hero_fine": "iPhone · iOS 26 or later · No account or brokerage connection required",
        "hero_alt": "Quantactic Markets screen showing a focused watchlist and local market context",
        "strip_label": "Quantactic research workflow",
        "metric_1_b": "What changed", "metric_1_s": "See unusual price, volume, trend, and market-context shifts.",
        "metric_2_b": "Why the move", "metric_2_s": "Put participation, trend, sector, and macro context around the move.",
        "metric_3_b": "Probabilistic outlook", "metric_3_s": "Explore 7-, 30-, and 90-day scenarios instead of one target.",
        "metric_4_b": "Model track record", "metric_4_s": "Compare completed forecasts with what actually happened.",
        "activity_h2": "Start with what changed.", "activity_p": "Quantactic compares recent market behavior with each symbol’s own baseline so you can spot meaningful shifts in price, volume, trend, volatility, and broader market context.",
        "activity_points": ["Recent activity versus normal", "Unusual price and volume behavior", "Trend and volatility-regime changes", "Watchlist changes since your last check"],
        "why_h2": "Understand why the move stands out.", "why_p": "Quantactic connects price action with participation, trend, sector behavior, broad-market context, and macro conditions without inventing a catalyst.",
        "why_points": ["Participation and relative strength", "Sector and benchmark context", "Macro conditions that shape the tape", "Clear invalidation when the context weakens"],
        "outlook_h2": "Explore what may happen next.", "outlook_p": "Quantactic generates probabilistic 7-, 30-, and 90-day scenarios from historical market behavior. Explore expected ranges, median outcomes, upside and downside paths, confidence, and the factors influencing the outlook.",
        "outlook_points": ["1,000 simulated paths", "Probability ranges, not a single target", "7-, 30-, and 90-day horizons", "Drivers and confidence kept visible"],
        "proof_eyebrow": "FORECAST ACCOUNTABILITY", "proof_h2": "See how the model actually performed.", "proof_p": "Quantactic keeps completed forecast records so you can compare previous outlooks with real market outcomes instead of seeing only today’s prediction.",
        "proof_points": ["Direction accuracy", "Median forecast error", "Expected-range coverage", "Performance by volatility regime"], "proof_note": "We keep the receipts—wins and misses stay visible.",
        "research_h2": "Research depth without the noise.", "research_p": "Keep the evidence close, explainable, and useful when you are deciding what deserves a closer look.",
        "research": [("Explainable signals", "Inspect trend conditions, factor contributions, risk context, invalidation conditions, and signal changes."), ("Compare in context", "Compare multiple stocks and ETFs from a common starting point instead of disconnected percentage moves."), ("Macro context", "Keep rates, volatility, the U.S. dollar, oil, economic releases, and market regime within reach."), ("Private on-device AI", "On supported devices, use Apple Intelligence for local explanations and research assistance without a third-party cloud AI provider.")],
        "pro_eyebrow": "QUANTACTIC PRO", "pro_h2": "Go deeper with your research.", "pro_p": "Quantactic Pro unlocks unlimited 7-day forecasts, full 30- and 90-day probabilistic outlooks, deeper model evidence, expanded private AI, higher research limits, and an ad-free experience.",
        "benefits": [("Full Forecasts", "Unlimited 7-day forecasts plus full 30- and 90-day scenarios, probability ranges, and deeper model detail."), ("Model Track Record", "Review completed forecasts, historical accuracy, median error, range coverage, and model behavior over time."), ("Deeper Signals", "See deeper factor detail, risk context, invalidation conditions, and signal changes."), ("Private AI + Uninterrupted Research", "Use expanded private AI, compare more assets, and remove interstitial ads.")],
        "annual_label": "Quantactic Pro Annual", "annual_value": "Best value", "annual_month": "About $3.33/month", "annual_save": "Save about 33%", "monthly_label": "Quantactic Pro Monthly", "monthly_value": "Flexible monthly access",
        "notice": "<b>For information and education only.</b> Quantactic provides market research and probabilistic analysis. It does not execute trades, connect to brokerage accounts, accept deposits, manage investments, or provide personalized investment advice. Forecasts, signals, and analysis are not guarantees of future results. Market data may be delayed or incomplete, and investing involves risk, including possible loss of principal.",
        "shot1": "See what changed", "shot2": "Explore what may happen next", "shot3": "Signals that show their work", "shot4": "Compare with context",
        "shot1_alt": "Quantactic Markets screen showing what changed", "shot2_alt": "Quantactic Forecast screen showing probabilistic scenarios", "shot3_alt": "Quantactic Signals screen showing evidence and risk context", "shot4_alt": "Quantactic Compare screen showing aligned performance",
        "footer_copy": "© 2026 Quantactic. All rights reserved.", "footer_privacy": "Privacy Policy", "footer_terms": "Terms of Use", "footer_support": "Support", "legal_eyebrow": "LEGAL",
        "privacy_h1": "Privacy Policy", "privacy_dates": "Effective date: July 30, 2026 · Last updated: August 9, 2026", "terms_h1": "Terms of Use", "terms_dates": "Effective date: July 30, 2026 · Last updated: August 9, 2026",
    },
    "es": {
        "brand": "Quantactic", "nav_product": "Producto", "nav_privacy": "Privacidad", "nav_terms": "Términos", "lang_label": "Idioma",
        "title_index": "Quantactic — Señales, pronósticos e inteligencia de mercado", "meta_index": "Quantactic te ayuda a descubrir qué cambió, entender movimientos inusuales, explorar escenarios probabilísticos de 7, 30 y 90 días y revisar cómo rindieron los pronósticos anteriores.", "title_privacy": "Política de privacidad — Quantactic", "meta_privacy": "Política de privacidad de Quantactic", "title_terms": "Términos de uso — Quantactic", "meta_terms": "Términos de uso de Quantactic",
        "hero_eyebrow": "INTELIGENCIA DE MERCADO QUE MUESTRA SU TRABAJO", "hero_h1_1": "Descubre qué cambió.", "hero_h1_2": "Entiende el movimiento.", "hero_h1_3": "Explora lo que viene.", "hero_lede": "Quantactic convierte la actividad del mercado, las señales explicables, los escenarios probabilísticos, la evidencia del modelo, las comparaciones, el contexto macro y la IA privada en el dispositivo en un flujo de investigación enfocado.", "cta_download": "Descargar en el App Store", "cta_explore": "Explorar Quantactic ↓", "hero_fine": "iPhone · iOS 26 o posterior · Sin cuenta ni conexión a un bróker", "hero_alt": "Pantalla Markets de Quantactic con lista de seguimiento y contexto de mercado local",
        "strip_label": "Flujo de investigación de Quantactic", "metric_1_b": "Qué cambió", "metric_1_s": "Detecta cambios inusuales de precio, volumen, tendencia y contexto.", "metric_2_b": "Por qué destaca el movimiento", "metric_2_s": "Añade participación, tendencia, sector y contexto macro.", "metric_3_b": "Pronóstico probabilístico", "metric_3_s": "Explora escenarios de 7, 30 y 90 días, no un único objetivo.", "metric_4_b": "Historial del modelo", "metric_4_s": "Compara pronósticos completados con lo que ocurrió.",
        "activity_h2": "Empieza por lo que cambió.", "activity_p": "Quantactic compara el comportamiento reciente con la línea base de cada activo para detectar cambios relevantes en precio, volumen, tendencia, volatilidad y contexto de mercado.", "activity_points": ["Actividad reciente frente a lo normal", "Comportamiento inusual de precio y volumen", "Cambios de tendencia y régimen de volatilidad", "Cambios desde tu última revisión"],
        "why_h2": "Entiende por qué destaca el movimiento.", "why_p": "Quantactic conecta precio, participación, tendencia, sector, mercado amplio y condiciones macro sin inventar un catalizador.", "why_points": ["Participación y fuerza relativa", "Contexto del sector y del índice", "Condiciones macro que influyen", "Invalidación clara cuando el contexto cambia"],
        "outlook_h2": "Explora lo que podría ocurrir después.", "outlook_p": "Quantactic genera escenarios probabilísticos de 7, 30 y 90 días a partir del comportamiento histórico. Explora rangos esperados, medianas, caminos alcistas y bajistas, confianza y factores del pronóstico.", "outlook_points": ["1.000 trayectorias simuladas", "Rangos de probabilidad, no un único objetivo", "Horizontes de 7, 30 y 90 días", "Factores y confianza visibles"],
        "proof_eyebrow": "RESPONSABILIDAD DEL PRONÓSTICO", "proof_h2": "Mira cómo rindió realmente el modelo.", "proof_p": "Quantactic conserva registros de pronósticos completados para comparar escenarios anteriores con resultados reales, no solo con la predicción de hoy.", "proof_points": ["Precisión de dirección", "Error mediano del pronóstico", "Cobertura del rango esperado", "Rendimiento por régimen de volatilidad"], "proof_note": "Conservamos los recibos: aciertos y fallos siguen visibles.",
        "research_h2": "Más profundidad, menos ruido.", "research_p": "Mantén la evidencia cerca, explicable y útil para decidir qué merece una mirada más atenta.", "research": [("Señales explicables", "Inspecciona tendencia, factores, contexto de riesgo, invalidación y cambios de señal."), ("Compara con contexto", "Compara acciones y ETF desde un mismo punto de partida, no porcentajes aislados."), ("Contexto macro", "Ten a mano tipos, volatilidad, dólar, petróleo, datos económicos y régimen de mercado."), ("IA privada en el dispositivo", "En dispositivos compatibles, usa Apple Intelligence para explicaciones locales sin un proveedor de IA en la nube de terceros.")],
        "pro_eyebrow": "QUANTACTIC PRO", "pro_h2": "Profundiza en tu investigación.", "pro_p": "Quantactic Pro desbloquea pronósticos ilimitados de 7 días, escenarios probabilísticos completos de 30 y 90 días, más evidencia del modelo, IA privada ampliada, mayores límites de investigación y una experiencia sin anuncios intersticiales.", "benefits": [("Pronósticos completos", "Pronósticos ilimitados de 7 días y escenarios completos de 30 y 90 días con rangos y más detalle."), ("Historial del modelo", "Revisa pronósticos completados, precisión histórica, error mediano, cobertura y comportamiento."), ("Señales más profundas", "Consulta factores, contexto de riesgo, invalidación y cambios de señal."), ("IA privada + investigación sin interrupciones", "Usa IA privada ampliada, compara más activos y elimina anuncios intersticiales.")],
        "annual_label": "Quantactic Pro Anual", "annual_value": "Mejor valor", "annual_month": "Aproximadamente $3,33/mes", "annual_save": "Ahorra aproximadamente 33%", "monthly_label": "Quantactic Pro Mensual", "monthly_value": "Acceso mensual flexible", "notice": "<b>Solo información y educación.</b> Quantactic ofrece investigación y análisis probabilístico. No ejecuta operaciones, conecta cuentas de bróker, acepta depósitos, gestiona inversiones ni ofrece asesoramiento personalizado. Los pronósticos, señales y análisis no garantizan resultados. Los datos pueden retrasarse o estar incompletos; invertir implica riesgo, incluida la pérdida de capital.", "shot1": "Descubre qué cambió", "shot2": "Explora lo que podría ocurrir", "shot3": "Señales que muestran su trabajo", "shot4": "Compara con contexto", "shot1_alt": "Pantalla Markets de Quantactic mostrando cambios", "shot2_alt": "Pantalla Forecast de Quantactic con escenarios probabilísticos", "shot3_alt": "Pantalla Signals de Quantactic con evidencia y riesgo", "shot4_alt": "Pantalla Compare de Quantactic con rendimiento alineado", "footer_copy": "© 2026 Quantactic. Todos los derechos reservados.", "footer_privacy": "Política de privacidad", "footer_terms": "Términos de uso", "footer_support": "Soporte", "legal_eyebrow": "LEGAL", "privacy_h1": "Política de privacidad", "privacy_dates": "Fecha de vigencia: 30 de julio de 2026 · Actualizada: 9 de agosto de 2026", "terms_h1": "Términos de uso", "terms_dates": "Fecha de vigencia: 30 de julio de 2026 · Actualizada: 9 de agosto de 2026",
    },
    "ja": {
        "brand": "クオンタクティック", "nav_product": "製品", "nav_privacy": "プライバシー", "nav_terms": "利用規約", "lang_label": "言語",
        "title_index": "クオンタクティック — 株式シグナルと予測・市場インテリジェンス", "meta_index": "市場の変化、値動きの背景、7・30・90日の確率ベースの見通し、過去の予測実績を確認できます。", "title_privacy": "プライバシーポリシー — クオンタクティック", "meta_privacy": "クオンタクティックのプライバシーポリシー", "title_terms": "利用規約 — クオンタクティック", "meta_terms": "クオンタクティックの利用規約",
        "hero_eyebrow": "根拠を示す市場インテリジェンス", "hero_h1_1": "市場で何が変わったか。", "hero_h1_2": "値動きの背景を理解する。", "hero_h1_3": "次の展開を探る。", "hero_lede": "クオンタクティックは、市場の動き、説明可能なシグナル、確率ベースの見通し、モデルの根拠、比較、マクロの文脈、オンデバイスのプライベートAIを一つのリサーチフローにまとめます。", "cta_download": "App Storeでダウンロード", "cta_explore": "クオンタクティックを見る ↓", "hero_fine": "iPhone · iOS 26以降 · アカウント・証券口座接続不要", "hero_alt": "ウォッチリストと市場の文脈を示すクオンタクティックのMarkets画面",
        "strip_label": "クオンタクティックのリサーチフロー", "metric_1_b": "市場の変化", "metric_1_s": "価格、出来高、トレンド、文脈の変化を確認。", "metric_2_b": "値動きの背景", "metric_2_s": "参加度、トレンド、セクター、マクロを重ねる。", "metric_3_b": "確率ベースの見通し", "metric_3_s": "単一目標ではなく7・30・90日のシナリオ。", "metric_4_b": "モデルの実績", "metric_4_s": "完了した予測と実際の結果を比較。",
        "activity_h2": "まず、何が変わったかを見る。", "activity_p": "クオンタクティックは各銘柄の基準値と最近の動きを比較し、価格、出来高、トレンド、ボラティリティ、市場全体の変化を見つけます。", "activity_points": ["通常との比較", "価格と出来高の異変", "トレンドとボラティリティ体制の変化", "前回確認してからの変化"],
        "why_h2": "値動きが目立つ背景を理解する。", "why_p": "価格の動きに参加度、トレンド、セクター、市場全体、マクロの条件を重ね、根拠のない材料を作りません。", "why_points": ["参加度と相対的な強さ", "セクターとベンチマークの文脈", "相場を形づくるマクロ条件", "文脈が崩れたときの無効化条件"],
        "outlook_h2": "次に起こり得る展開を探る。", "outlook_p": "過去の市場行動から7・30・90日の確率ベースのシナリオを生成。予想レンジ、中央値、上下の経路、確信度、見通しの要因を確認できます。", "outlook_points": ["1,000本のシミュレーション経路", "単一目標ではなく確率レンジ", "7・30・90日の期間", "要因と確信度を表示"],
        "proof_eyebrow": "予測の説明責任", "proof_h2": "モデルの実績を確かめる。", "proof_p": "完了した予測を保存し、過去の見通しと実際の結果を比較できます。今日の予測だけではありません。", "proof_points": ["方向精度", "予測の中央値誤差", "予想レンジのカバー率", "ボラティリティ体制別の実績"], "proof_note": "良い結果も外れも、記録を残します。",
        "research_h2": "ノイズなしで、リサーチを深く。", "research_p": "根拠を手元に置き、説明可能で、次に調べる価値を判断できる形にします。", "research": [("説明可能なシグナル", "トレンド、要因、リスク、無効化条件、シグナルの変化を確認。"), ("文脈で比較", "株式やETFを同じ起点から比較し、離れたパーセント表示に頼らない。"), ("マクロの文脈", "金利、ボラティリティ、ドル、原油、経済指標、市場レジームを確認。"), ("オンデバイスのプライベートAI", "対応端末ではApple Intelligenceで、第三者クラウドAIに送らず説明とリサーチを支援します。")],
        "pro_eyebrow": "クオンタクティック PRO", "pro_h2": "リサーチを、さらに深く。", "pro_p": "クオンタクティック Proは、7日予測の無制限利用、30日・90日の確率ベースの見通し、深いモデル根拠、拡張されたプライベートAI、より高いリサーチ上限、広告なしの体験を解放します。", "benefits": [("完全な予測", "7日予測を無制限に利用し、30日・90日のシナリオ、確率レンジ、詳細な根拠を確認。"), ("モデルの実績", "完了した予測、過去の精度、中央値誤差、レンジ内率、時間による挙動を確認。"), ("深いシグナル", "要因、リスク、無効化条件、シグナルの変化を詳しく見る。"), ("プライベートAI + 途切れないリサーチ", "拡張AIを使い、より多くの銘柄を比較し、インタースティシャル広告を削除。")],
        "annual_label": "クオンタクティック Pro 年額", "annual_value": "継続利用に最適", "annual_month": "月あたり約$3.33", "annual_save": "約33%お得", "monthly_label": "クオンタクティック Pro 月額", "monthly_value": "柔軟な月額アクセス", "notice": "<b>情報・教育目的のみ。</b> クオンタクティックは市場リサーチと確率分析を提供します。取引の執行、証券口座への接続、入金の受け入れ、資産管理、個別の投資助言は行いません。予測・シグナル・分析は将来の結果を保証しません。市場データは遅延または不完全な場合があり、投資には元本損失を含むリスクがあります。", "shot1": "市場の変化を見る", "shot2": "次の展開を探る", "shot3": "根拠を示すシグナル", "shot4": "文脈で比較", "shot1_alt": "市場の変化を示すクオンタクティックMarkets画面", "shot2_alt": "確率シナリオを示すクオンタクティックForecast画面", "shot3_alt": "根拠とリスクを示すクオンタクティックSignals画面", "shot4_alt": "整列したパフォーマンスを示すクオンタクティックCompare画面", "footer_copy": "© 2026 クオンタクティック. All rights reserved.", "footer_privacy": "プライバシーポリシー", "footer_terms": "利用規約", "footer_support": "サポート", "legal_eyebrow": "LEGAL", "privacy_h1": "プライバシーポリシー", "privacy_dates": "施行日: 2026年7月30日 · 最終更新: 2026年8月9日", "terms_h1": "利用規約", "terms_dates": "施行日: 2026年7月30日 · 最終更新: 2026年8月9日",
    },
    "ko": {
        "brand": "퀀트택틱", "nav_product": "제품", "nav_privacy": "개인정보", "nav_terms": "이용약관", "lang_label": "언어",
        "title_index": "퀀트택틱 — 주식 시그널과 전망·시장 인텔리전스", "meta_index": "퀀트택틱으로 무엇이 달라졌는지 보고, 움직임의 맥락을 이해하고, 7·30·90일 확률 기반 전망과 과거 모델 성과를 확인하세요.", "title_privacy": "개인정보 처리방침 — 퀀트택틱", "meta_privacy": "퀀트택틱 개인정보 처리방침", "title_terms": "이용약관 — 퀀트택틱", "meta_terms": "퀀트택틱 이용약관",
        "hero_eyebrow": "근거를 보여주는 시장 인텔리전스", "hero_h1_1": "무엇이 달라졌는지 보고.", "hero_h1_2": "움직임의 맥락을 이해하고.", "hero_h1_3": "다음 가능성을 살펴보세요.", "hero_lede": "퀀트택틱은 시장 활동, 설명 가능한 시그널, 확률 기반 전망, 모델 근거, 비교, 매크로 맥락, 온디바이스 프라이빗 AI를 하나의 집중된 리서치 흐름으로 묶습니다.", "cta_download": "App Store에서 다운로드", "cta_explore": "퀀트택틱 살펴보기 ↓", "hero_fine": "iPhone · iOS 26 이상 · 계정 및 증권 계좌 연결 불필요", "hero_alt": "관심종목과 시장 맥락을 보여주는 퀀트택틱 Markets 화면",
        "strip_label": "퀀트택틱 리서치 흐름", "metric_1_b": "무엇이 달라졌나", "metric_1_s": "가격·거래량·추세·시장 맥락 변화를 확인합니다.", "metric_2_b": "움직임의 맥락", "metric_2_s": "참여도·추세·섹터·매크로를 함께 봅니다.", "metric_3_b": "확률 기반 전망", "metric_3_s": "하나의 목표가 아닌 7·30·90일 시나리오를 봅니다.", "metric_4_b": "모델 성과", "metric_4_s": "완료된 전망과 실제 결과를 비교합니다.",
        "activity_h2": "무엇이 달라졌는지부터 보세요.", "activity_p": "퀀트택틱은 최근 시장 행동을 종목별 기준선과 비교해 가격, 거래량, 추세, 변동성, 시장 맥락의 의미 있는 변화를 찾습니다.", "activity_points": ["평소와 비교한 최근 활동", "비정상적인 가격·거래량", "추세와 변동성 국면 변화", "마지막 확인 이후 관심종목 변화"],
        "why_h2": "왜 이 움직임이 두드러지는지 이해하세요.", "why_p": "가격 움직임에 참여도, 추세, 섹터, 시장 전체, 매크로 조건을 연결하며 확인되지 않은 재료를 만들어내지 않습니다.", "why_points": ["참여도와 상대 강도", "섹터와 벤치마크 맥락", "시장 흐름을 만드는 매크로 조건", "맥락이 약해질 때의 무효화 조건"],
        "outlook_h2": "다음 가능성을 살펴보세요.", "outlook_p": "과거 시장 행동을 바탕으로 7·30·90일 확률 기반 시나리오를 생성합니다. 예상 범위, 중앙값, 상승·하락 경로, 신뢰도와 전망 요인을 확인하세요.", "outlook_points": ["1,000개 시뮬레이션 경로", "단일 목표가 아닌 확률 범위", "7·30·90일 전망 기간", "요인과 신뢰도 공개"],
        "proof_eyebrow": "전망의 책임성", "proof_h2": "모델이 실제로 어떻게 작동했는지 보세요.", "proof_p": "퀀트택틱은 완료된 전망을 저장해 과거 전망과 실제 시장 결과를 비교합니다. 오늘의 예측만 보여주지 않습니다.", "proof_points": ["방향 정확도", "전망 중앙값 오차", "예상 범위 커버리지", "변동성 국면별 성과"], "proof_note": "맞은 결과와 빗나간 결과를 모두 기록합니다.",
        "research_h2": "소음 없이 더 깊은 리서치.", "research_p": "근거를 가까이 두고, 설명 가능하고, 다음에 무엇을 살펴볼지 판단할 수 있게 합니다.", "research": [("설명 가능한 시그널", "추세, 요인 기여, 리스크 맥락, 무효화 조건과 시그널 변화를 확인하세요."), ("맥락 속 비교", "주식과 ETF를 같은 출발점에서 비교해 단절된 수익률만 보지 않습니다."), ("매크로 맥락", "금리, 변동성, 달러, 원유, 경제 발표와 시장 국면을 한곳에 둡니다."), ("온디바이스 프라이빗 AI", "지원 기기에서는 제3자 클라우드 AI 없이 Apple Intelligence로 설명과 리서치를 도울 수 있습니다.")],
        "pro_eyebrow": "퀀트택틱 PRO", "pro_h2": "리서치를 더 깊게 하세요.", "pro_p": "퀀트택틱 Pro는 7일 전망 무제한, 30·90일 전체 확률 기반 전망, 더 깊은 모델 근거, 확장된 프라이빗 AI, 높은 리서치 한도와 광고 없는 경험을 제공합니다.", "benefits": [("전체 전망", "7일 전망 무제한과 30·90일 시나리오, 확률 범위, 더 깊은 모델 상세를 제공합니다."), ("모델 성과", "완료된 전망, 과거 정확도, 중앙값 오차, 범위 커버리지와 시간에 따른 행동을 검토합니다."), ("더 깊은 시그널", "요인, 리스크 맥락, 무효화 조건과 시그널 변화를 확인합니다."), ("프라이빗 AI + 끊김 없는 리서치", "확장된 프라이빗 AI를 사용하고 더 많은 자산을 비교하며 전면 광고를 제거합니다.")],
        "annual_label": "퀀트택틱 Pro 연간", "annual_value": "지속적인 리서치에 최적", "annual_month": "월 약 $3.33", "annual_save": "약 33% 절약", "monthly_label": "퀀트택틱 Pro 월간", "monthly_value": "유연한 월간 이용", "notice": "<b>정보 및 교육 목적만을 위한 서비스입니다.</b> 퀀트택틱은 시장 리서치와 확률 분석을 제공합니다. 거래를 실행하거나 증권 계좌에 연결하거나 입금을 받거나 자산을 관리하거나 개인 맞춤 투자 조언을 제공하지 않습니다. 전망·시그널·분석은 미래 결과를 보장하지 않습니다. 시장 데이터는 지연되거나 불완전할 수 있으며 투자에는 원금 손실을 포함한 위험이 있습니다.", "shot1": "무엇이 달라졌는지 확인", "shot2": "다음 가능성 살펴보기", "shot3": "근거를 보여주는 시그널", "shot4": "맥락 속에서 비교", "shot1_alt": "변화를 보여주는 퀀트택틱 Markets 화면", "shot2_alt": "확률 시나리오를 보여주는 퀀트택틱 Forecast 화면", "shot3_alt": "근거와 위험을 보여주는 퀀트택틱 Signals 화면", "shot4_alt": "성과를 정렬해 보여주는 퀀트택틱 Compare 화면", "footer_copy": "© 2026 퀀트택틱. All rights reserved.", "footer_privacy": "개인정보 처리방침", "footer_terms": "이용약관", "footer_support": "지원", "legal_eyebrow": "LEGAL", "privacy_h1": "개인정보 처리방침", "privacy_dates": "시행일: 2026년 7월 30일 · 최종 업데이트: 2026년 8월 9일", "terms_h1": "이용약관", "terms_dates": "시행일: 2026년 7월 30일 · 최종 업데이트: 2026년 8월 9일",
    },
    "zh-Hans": {
        "brand": "Quantactic", "nav_product": "产品", "nav_privacy": "隐私", "nav_terms": "条款", "lang_label": "语言",
        "title_index": "Quantactic — 股票信号、走势预测与市场情报", "meta_index": "Quantactic 帮助你了解市场发生了什么变化、理解异常波动、探索 7、30、90 天概率型走势预测，并查看历史预测的实际表现。", "title_privacy": "隐私政策 — Quantactic", "meta_privacy": "Quantactic 隐私政策", "title_terms": "使用条款 — Quantactic", "meta_terms": "Quantactic 使用条款",
        "hero_eyebrow": "展示依据的市场情报", "hero_h1_1": "了解发生了什么变化。", "hero_h1_2": "理解波动的背景。", "hero_h1_3": "探索接下来可能发生什么。", "hero_lede": "Quantactic 将市场活动、可解释信号、概率型走势预测、模型依据、对比、宏观背景与设备端私密 AI 汇聚到一个专注的研究流程中。", "cta_download": "在 App Store 下载", "cta_explore": "探索 Quantactic ↓", "hero_fine": "iPhone · iOS 26 或更高版本 · 无需账户或券商连接", "hero_alt": "显示自选股与本地市场背景的 Quantactic Markets 页面",
        "strip_label": "Quantactic 研究流程", "metric_1_b": "市场变化", "metric_1_s": "查看价格、成交量、趋势和市场背景的异常变化。", "metric_2_b": "波动背景", "metric_2_s": "将参与度、趋势、行业与宏观背景放在一起。", "metric_3_b": "概率型走势预测", "metric_3_s": "探索 7、30、90 天情景，而不是一个目标价。", "metric_4_b": "模型历史表现", "metric_4_s": "将已完成预测与实际结果进行比较。",
        "activity_h2": "先看市场发生了什么变化。", "activity_p": "Quantactic 将近期市场行为与每个标的自身基线比较，帮助你发现价格、成交量、趋势、波动率和更广泛市场背景的有意义变化。", "activity_points": ["近期活动与正常状态的比较", "异常的价格与成交量行为", "趋势和波动率状态变化", "自上次查看以来的自选变化"],
        "why_h2": "理解为什么这次波动值得关注。", "why_p": "Quantactic 将价格走势与参与度、趋势、行业行为、大盘背景和宏观条件连接起来，不虚构事件原因。", "why_points": ["参与度与相对强度", "行业和基准背景", "影响市场的宏观条件", "背景减弱时清晰的失效条件"],
        "outlook_h2": "探索接下来可能发生什么。", "outlook_p": "Quantactic 根据历史市场行为生成 7、30、90 天概率型走势预测。查看预期区间、中位结果、上下行路径、置信度以及影响预测的因素。", "outlook_points": ["1,000 条模拟路径", "概率范围，而不是单一目标价", "7、30、90 天预测周期", "保留驱动因素和置信度"],
        "proof_eyebrow": "预测问责", "proof_h2": "查看模型的真实表现。", "proof_p": "Quantactic 保存已完成的预测记录，让你将过去的展望与实际市场结果比较，而不是只看到今天的预测。", "proof_points": ["方向准确率", "预测中位误差", "预期区间覆盖率", "不同波动状态下的表现"], "proof_note": "好的结果和失败案例都会保留。",
        "research_h2": "更深的研究，没有多余噪音。", "research_p": "把依据放在手边，以可解释、可操作的方式判断下一步值得研究什么。", "research": [("可解释信号", "查看趋势条件、因素贡献、风险背景、失效条件与信号变化。"), ("在背景中比较", "从同一起点比较股票和 ETF，而不是依赖互不相连的涨跌幅。"), ("宏观背景", "将利率、波动率、美元、原油、经济数据和市场状态放在手边。"), ("设备端私密 AI", "在支持的设备上使用 Apple Intelligence 获得本地解释与研究辅助，不依赖第三方云端 AI。")],
        "pro_eyebrow": "QUANTACTIC PRO", "pro_h2": "深入你的研究。", "pro_p": "Quantactic Pro 解锁无限 7 日预测、完整 30 日和 90 日概率型走势预测、更深入的模型依据、扩展的设备端私密 AI、更高的研究额度以及无插页广告体验。", "benefits": [("完整预测", "无限 7 日预测，以及完整的 30、90 日情景、概率范围和更深入的模型细节。"), ("模型历史表现", "查看已完成预测、历史准确率、中位误差、区间覆盖率和模型随时间的行为。"), ("更深入的信号", "查看更完整的因素细节、风险背景、失效条件和信号变化。"), ("私密 AI + 不间断研究", "使用扩展的设备端私密 AI，比较更多资产，并移除插页广告。")],
        "annual_label": "Quantactic Pro 年度", "annual_value": "持续研究的最佳选择", "annual_month": "约合每月 $3.33", "annual_save": "约节省 33%", "monthly_label": "Quantactic Pro 月度", "monthly_value": "灵活的月度使用", "notice": "<b>仅供信息与教育用途。</b> Quantactic 提供市场研究与概率分析，不执行交易、不连接券商账户、不接受存款、不管理投资，也不提供个性化投资建议。预测、信号和分析不保证未来结果。市场数据可能延迟或不完整，投资有风险，包括本金损失。", "shot1": "了解市场变化", "shot2": "探索接下来可能发生什么", "shot3": "展示依据的市场信号", "shot4": "在背景中比较", "shot1_alt": "展示市场变化的 Quantactic Markets 页面", "shot2_alt": "展示概率情景的 Quantactic Forecast 页面", "shot3_alt": "展示依据和风险背景的 Quantactic Signals 页面", "shot4_alt": "展示对齐表现的 Quantactic Compare 页面", "footer_copy": "© 2026 Quantactic. 保留所有权利。", "footer_privacy": "隐私政策", "footer_terms": "使用条款", "footer_support": "支持", "legal_eyebrow": "LEGAL", "privacy_h1": "隐私政策", "privacy_dates": "生效日期：2026 年 7 月 30 日 · 最后更新：2026 年 8 月 9 日", "terms_h1": "使用条款", "terms_dates": "生效日期：2026 年 7 月 30 日 · 最后更新：2026 年 8 月 9 日",
    },
}

REQUIRED_KEYS = set(CONTENT["en"])
for _code, _copy in CONTENT.items():
    missing = REQUIRED_KEYS - set(_copy)
    if missing:
        raise RuntimeError(f"{_code} is missing content keys: {sorted(missing)}")


def asset_prefix(in_locale_folder: bool) -> str:
    return "../" if in_locale_folder else ""


def lang_switcher(current: str, page: str, in_locale_folder: bool) -> str:
    file = "index.html" if page == "index" else f"{page}.html"
    links = []
    for lang in LANGS:
        code = lang["code"]
        href = file if in_locale_folder and code == current else (f"../{code}/{file}" if in_locale_folder else f"{code}/{file}")
        current_attr = ' aria-current="true"' if code == current else ""
        links.append(f'<a href="{href}" hreflang="{lang["html_lang"]}"{current_attr}>{lang["label"]}</a>')
    label = next(lang["short"] for lang in LANGS if lang["code"] == current)
    return f'<details class="lang-switch"><summary aria-label="{CONTENT[current]["lang_label"]}">{label}</summary><div class="lang-menu" role="menu">{"".join(links)}</div></details>'


def nav(c: dict, current: str, page: str, in_locale_folder: bool) -> str:
    p = asset_prefix(in_locale_folder)
    product_href = "#product" if page == "index" else "index.html#product"
    return f'''<nav class="nav" aria-label="{c["nav_product"]}">
      <a class="brand" href="index.html" aria-label="{c["brand"]} home"><span class="mark"><img src="{p}assets/quant-app-icon.png" alt=""></span>{c["brand"]}</a>
      <div class="nav-right"><div class="nav-links"><a href="{product_href}">{c["nav_product"]}</a><a href="privacy.html">{c["nav_privacy"]}</a><a href="terms.html">{c["nav_terms"]}</a></div>{lang_switcher(current, page, in_locale_folder)}</div>
    </nav>'''


def head(c: dict, title: str, description: str, in_locale_folder: bool, page: str, lang_code: str) -> str:
    p = asset_prefix(in_locale_folder)
    html_lang = next(lang["html_lang"] for lang in LANGS if lang["code"] == lang_code)
    alternate = []
    file = "index.html" if page == "index" else f"{page}.html"
    for lang in LANGS:
        target = f"../{lang['code']}/{file}" if in_locale_folder else f"{lang['code']}/{file}"
        alternate.append(f'<link rel="alternate" hreflang="{lang["html_lang"]}" href="{target}">')
    default = f"../en/{file}" if in_locale_folder else f"en/{file}"
    alternate.append(f'<link rel="alternate" hreflang="x-default" href="{default}">')
    return f'''<!doctype html>
<html lang="{html_lang}">
<head>
  <meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="{description}"><title>{title}</title>
  <link rel="stylesheet" href="{p}css/site.css">
  {"".join(alternate)}
</head>
<body>'''


def bullet_list(items: list[str]) -> str:
    return "<ul class=\"points\">" + "".join(f"<li>{item}</li>" for item in items) + "</ul>"


def index_page(lang_code: str, in_locale_folder: bool) -> str:
    c = CONTENT[lang_code]
    p = asset_prefix(in_locale_folder)
    # Only use localized screenshots where the repository actually has them;
    # surrounding copy and alt text remain localized without fabricating UI.
    asset_locale = lang_code if (ROOT / "assets" / lang_code).is_dir() else "en"
    feature_cards = "".join(f'<article class="feature"><div class="icon">{icon}</div><h3>{title}</h3><p>{body}</p></article>' for icon, (title, body) in zip(("⌁", "↗", "◌", "◈"), c["research"]))
    benefits = "".join(f'<article class="benefit"><h3>{title}</h3><p>{body}</p></article>' for title, body in c["benefits"])
    metrics = "".join(f'<div class="metric"><b>{c[f"metric_{i}_b"]}</b><span>{c[f"metric_{i}_s"]}</span></div>' for i in range(1, 5))
    stories = [
        ("activity_h2", "activity_p", "activity_points", "01-market-one-sharp-view.png", "shot1_alt"),
        ("why_h2", "why_p", "why_points", "03-signals-show-their-work.png", "shot3_alt"),
        ("outlook_h2", "outlook_p", "outlook_points", "02-see-what-may-happen-next.png", "shot2_alt"),
        ("proof_h2", "proof_p", "proof_points", "04-compare-with-context.png", "shot4_alt"),
    ]
    story_chunks = []
    for key, body_key, points_key, asset, alt_key in stories:
        eyebrow = f'<div class="eyebrow">{c["proof_eyebrow"]}</div>' if key == "proof_h2" else ""
        note = f'<p class="proof-note">{c["proof_note"]}</p>' if key == "proof_h2" else ""
        alt = c[alt_key]
        story_chunks.append(f'<section class="section story"><div class="story-copy">{eyebrow}<h2>{c[key]}</h2><p>{c[body_key]}</p>{bullet_list(c[points_key])}{note}</div><img src="{p}assets/{asset_locale}/{asset}" alt="{alt}"></section>')
    story_html = "".join(story_chunks)
    return head(c, c["title_index"], c["meta_index"], in_locale_folder, "index", lang_code) + f'''<div class="shell">
    {nav(c, lang_code, "index", in_locale_folder)}
    <main>
      <section class="hero"><div><div class="eyebrow"><span class="dot"></span>{c["hero_eyebrow"]}</div><h1>{c["hero_h1_1"]}<br><em>{c["hero_h1_2"]}</em><br>{c["hero_h1_3"]}</h1><p class="lede">{c["hero_lede"]}</p><div class="actions"><a class="button" href="{APP_STORE_URL}">{c["cta_download"]}</a><a class="text-link" href="#product">{c["cta_explore"]}</a></div><p class="fine">{c["hero_fine"]}</p></div><div class="hero-shot"><img src="{p}assets/{asset_locale}/01-market-one-sharp-view.png" alt="{c["hero_alt"]}"></div></section>
    </main>
  </div>
  <section class="strip" aria-label="{c["strip_label"]}"><div class="shell strip-inner">{metrics}</div></section>
  <main class="shell" id="product">
    {story_html}
    <section class="section"><div class="section-heading"><h2>{c["research_h2"]}</h2><p>{c["research_p"]}</p></div><div class="feature-grid">{feature_cards}</div></section>
    <section class="section"><div class="pro"><div><div class="eyebrow">{c["pro_eyebrow"]}</div><h2>{c["pro_h2"]}</h2><p>{c["pro_p"]}</p><div class="benefit-grid">{benefits}</div></div><div class="price-block"><div class="price annual"><b>{c["annual_label"]}</b><strong>$39.99<span>/ year</span></strong><small>{c["annual_month"]} · {c["annual_save"]}<br>{c["annual_value"]}</small></div><div class="price monthly"><b>{c["monthly_label"]}</b><strong>$4.99<span>/ month</span></strong><small>{c["monthly_value"]}</small></div></div></div></section>
    <aside class="notice">{c["notice"]}</aside>
  </main>
  <footer><div class="shell footer-row"><span>{c["footer_copy"]}</span><span class="footer-links"><a href="privacy.html">{c["footer_privacy"]}</a><a href="terms.html">{c["footer_terms"]}</a><a href="mailto:{SUPPORT_EMAIL}">{c["footer_support"]}</a></span></div></footer>
</body></html>'''


def legal_page(lang_code: str, kind: str, in_locale_folder: bool) -> str:
    c = CONTENT[lang_code]
    p = asset_prefix(in_locale_folder)
    body = EN_PRIVACY if lang_code == "en" and kind == "privacy" else EN_TERMS if lang_code == "en" else LEGAL_BODIES[lang_code][kind]
    title = c[f"title_{kind}"]; meta = c[f"meta_{kind}"]; h1 = c[f"{kind}_h1"]; dates = c[f"{kind}_dates"]
    other = "terms.html" if kind == "privacy" else "privacy.html"; other_label = c["footer_terms"] if kind == "privacy" else c["footer_privacy"]
    return head(c, title, meta, in_locale_folder, kind, lang_code) + f'''<div class="shell legal">
    {nav(c, lang_code, kind, in_locale_folder)}
    <header class="legal-hero"><div class="eyebrow">{c["legal_eyebrow"]}</div><h1>{h1}</h1><p>{dates}</p></header>
    <article class="legal">{body}</article>
    <footer class="legal-footer">© 2026 {c["brand"]} · <a class="link" href="index.html">{c["nav_product"]}</a> · <a class="link" href="{other}">{other_label}</a></footer>
  </div></body></html>'''


EN_PRIVACY = '''<div class="callout">Quantactic is designed as a no-account market-research app. Your research history and supported AI interactions are designed to remain local where described, while market data, macro data, ads, purchases, and other third-party services use network connections as required.</div>
<h2>1. Who we are</h2><p>Quantactic is an iPhone market-analysis application. For privacy questions, contact <a href="mailto:xjimmypark@gmail.com">xjimmypark@gmail.com</a>.</p>
<h2>2. Information stored on your device</h2><p>Quantactic stores watchlists, settings, notification preferences, language preference, saved forecast records, and selected research views locally. Supported provider credentials, if you enter them, are stored using the iOS Keychain. AI conversation content is handled according to the feature and device processing described in this policy.</p><p>Quantactic does not require an account, connect to brokerage accounts, or store payment-card information.</p>
<h2>3. Network services</h2><p>Market data, charts, search, headlines, and macroeconomic series require network requests to market-data providers and FRED. Those providers may receive the symbol or series requested and technical information under their own policies.</p>
<h2>4. Advertising</h2><p>Eligible users without Quantactic Pro may see interstitial advertising through Google Mobile Ads. Google and its partners may process information for delivery, measurement, fraud prevention, and personalization under their policies and your device settings.</p><p>See <a href="https://policies.google.com/privacy">Google’s Privacy Policy</a>.</p>
<h2>5. Purchases</h2><p>Quantactic Pro Monthly and Quantactic Pro Annual are processed by Apple through StoreKit and the App Store. Quantactic does not receive or store your payment-card number. U.S. reference prices are $4.99 per month and $39.99 per year; regional prices are shown by Apple.</p>
<h2>6. Apple Intelligence and local AI</h2><p>On supported devices, Quantactic uses Apple Intelligence and Foundation Models for on-device explanations and research assistance. Quantactic does not send supported AI prompts to a third-party cloud AI provider. Availability depends on Apple’s device settings and policies.</p>
<h2>7. Notifications and sharing</h2><p>Notifications are optional and use local iOS notifications for features you enable. Quantactic does not continuously monitor a portfolio on a server while the app is closed. If you share an image or link, iOS sends it to the destination you select.</p>
<h2>8. Retention and deletion</h2><p>Local preferences and saved research remain on your device until changed or the app is deleted. Quantactic does not operate a user-account database for this local history.</p>
<h2>9. Children and changes</h2><p>Quantactic is not directed to children. We may update this policy as the product changes and will revise the date above.</p>
<h2>10. Contact</h2><p>For privacy questions, email <a href="mailto:xjimmypark@gmail.com">xjimmypark@gmail.com</a>.</p>'''

EN_TERMS = '''<div class="callout"><strong>Important:</strong> Quantactic is an informational market-analysis and research tool. It is not a broker, investment adviser, trading platform, or recommendation service.</div>
<h2>1. Agreement and Apple’s standard EULA</h2><p>These Terms govern your use of Quantactic. The app is licensed, not sold, through the Apple App Store. The <a href="https://www.apple.com/legal/internet-services/itunes/dev/stdeula/">Apple Licensed Application End User License Agreement</a> applies unless a valid custom agreement supersedes it.</p>
<h2>2. Informational use only</h2><p>Quotes, charts, news, macro data, signals, forecasts, and AI responses are general informational and educational analysis. They are not personalized investment, legal, tax, accounting, or financial advice. Quantactic does not execute trades, connect to brokerage accounts, accept deposits, or manage investments.</p>
<h2>3. Signals, forecasts, and AI</h2><ul><li>Market information may be delayed, incomplete, unavailable, or inaccurate.</li><li>Signals describe analytical conditions; they are not offers or recommendations to buy or sell.</li><li>Forecasts are probabilistic scenarios derived from historical market behavior. They are not guaranteed predictions, price targets, trading instructions, or investment advice.</li><li>AI explanations are convenience features. Review them independently and do not rely on them as professional advice.</li></ul>
<h2>4. Quantactic Pro subscriptions</h2><p>Quantactic Pro Monthly costs $4.99 per month and Quantactic Pro Annual costs $39.99 per year in the United States, or the regional price shown by Apple. Both unlock the same Pro feature tier and differ only in billing period and price. Payment is charged through your Apple Account. Subscriptions automatically renew unless cancelled at least 24 hours before the end of the current billing period. Manage or cancel through Apple subscription settings. Use <strong>Restore Purchases</strong> in Quantactic when eligible.</p><p>Pro includes unlimited 7-day forecasts, full 30- and 90-day probabilistic outlooks, deeper model evidence, expanded private AI, higher research limits, and an ad-free experience.</p>
<div class="table"><table><thead><tr><th>Subscription</th><th>U.S. reference</th></tr></thead><tbody><tr><td>Quantactic Pro Monthly</td><td>$4.99 per month</td></tr><tr><td>Quantactic Pro Annual</td><td>$39.99 per year</td></tr><tr><td>Renewal</td><td>Automatically renews unless cancelled at least 24 hours before period end.</td></tr><tr><td>Restore</td><td>Use Restore Purchases in Quantactic.</td></tr></tbody></table></div>
<h2>5. Third-party services</h2><p>Quantactic may contact market-data, macro-data, advertising, Apple, and App Store services. Those services have their own terms and policies, and we do not guarantee their availability or accuracy.</p>
<h2>6. Availability and liability</h2><p>Features and data sources may change or be unavailable. To the maximum extent permitted by law, Quantactic is provided on an “as is” and “as available” basis. Quantactic and its developer are not liable for indirect losses, lost profits, trading losses, or business interruption arising from use of the app.</p>
<h2>7. Changes and contact</h2><p>We may update these Terms as Quantactic changes. Continued use after an update means you accept the revised Terms to the extent permitted by law. Questions: <a href="mailto:xjimmypark@gmail.com">xjimmypark@gmail.com</a>.</p>'''

LEGAL_BODIES = {
    "es": {
        "privacy": '''<div class="callout">Quantactic es una app de investigación de mercado sin cuenta. El historial de investigación y las interacciones compatibles con IA están diseñados para permanecer locales cuando se indica; los datos de mercado, macro, anuncios, compras y otros servicios usan la red cuando es necesario.</div><h2>1. Quiénes somos</h2><p>Quantactic es una aplicación de análisis de mercado para iPhone. Para preguntas de privacidad, escriba a <a href="mailto:xjimmypark@gmail.com">xjimmypark@gmail.com</a>.</p><h2>2. Información local</h2><p>Quantactic guarda localmente listas, ajustes, preferencias, registros de pronósticos y vistas de investigación. Las credenciales opcionales se guardan en el Llavero de iOS. No requiere cuenta, conecta con brókers ni almacena tarjetas.</p><h2>3. Servicios de red</h2><p>Las cotizaciones, gráficos, noticias y series macro requieren solicitudes a proveedores de datos y FRED. Esos proveedores pueden recibir el símbolo solicitado y metadatos técnicos según sus políticas.</p><h2>4. Publicidad y compras</h2><p>Usuarios sin Quantactic Pro pueden ver anuncios intersticiales de Google Mobile Ads. Quantactic Pro Monthly y Quantactic Pro Annual se procesan mediante Apple StoreKit; no recibimos el número de su tarjeta. Precios de referencia: 4,99 USD al mes y 39,99 USD al año.</p><h2>5. Apple Intelligence</h2><p>En dispositivos compatibles, Apple Intelligence y Foundation Models ofrecen explicaciones en el dispositivo. Quantactic no envía prompts compatibles a una IA en la nube de terceros.</p><h2>6. Notificaciones y eliminación</h2><p>Las notificaciones son locales y opcionales. No existe monitorización continua en un servidor. Las preferencias y el historial local permanecen hasta que se cambien o se elimine la app. Para preguntas: <a href="mailto:xjimmypark@gmail.com">xjimmypark@gmail.com</a>.</p>''',
        "terms": '''<div class="callout"><strong>Importante:</strong> Quantactic es una herramienta informativa de análisis e investigación de mercado. No es bróker, asesor de inversiones, plataforma de trading ni servicio de recomendaciones.</div><h2>1. Acuerdo y EULA de Apple</h2><p>Estos Términos rigen Quantactic, que se licencia a través del App Store. Aplica el <a href="https://www.apple.com/legal/internet-services/itunes/dev/stdeula/">EULA de aplicaciones con licencia de Apple</a>.</p><h2>2. Uso informativo</h2><p>Cotizaciones, gráficos, noticias, macro, señales, pronósticos y respuestas de IA son análisis generales informativos y educativos. No son asesoramiento personalizado. Quantactic no ejecuta operaciones, conecta cuentas de bróker, acepta depósitos ni gestiona inversiones.</p><h2>3. Señales y pronósticos</h2><ul><li>La información puede retrasarse, estar incompleta o ser inexacta.</li><li>Las señales describen condiciones analíticas, no recomendaciones.</li><li>Los pronósticos son escenarios probabilísticos derivados del comportamiento histórico, no objetivos de precio, instrucciones de trading ni garantías.</li><li>Revise las explicaciones de IA de forma independiente.</li></ul><h2>4. Suscripciones Quantactic Pro</h2><p><strong>Quantactic Pro Monthly</strong> cuesta 4,99 USD al mes y <strong>Quantactic Pro Annual</strong> cuesta 39,99 USD al año en EE. UU. Ambas desbloquean el mismo nivel Pro. Se renuevan automáticamente salvo cancelación al menos 24 horas antes del final del periodo. Gestione la suscripción en Apple y use Restaurar compras en Quantactic.</p><p>Pro ofrece pronósticos ilimitados de 7 días, escenarios probabilísticos completos de 30 y 90 días, evidencia del modelo, IA privada ampliada, mayores límites y experiencia sin anuncios.</p><h2>5. Servicios, disponibilidad y contacto</h2><p>Los servicios de terceros tienen sus propias políticas. Las funciones y datos pueden cambiar o no estar disponibles. Para preguntas: <a href="mailto:xjimmypark@gmail.com">xjimmypark@gmail.com</a>.</p>''',
    },
    "ja": {
        "privacy": '''<div class="callout">クオンタクティックはアカウント不要の市場リサーチアプリです。説明した範囲のリサーチ履歴とAIのやり取りは端末内に保たれるよう設計されていますが、市場データ、マクロ、広告、購入、第三者サービスには必要なネットワーク接続があります。</div><h2>1. 運営者</h2><p>クオンタクティックはiPhone向け市場分析アプリです。お問い合わせは <a href="mailto:xjimmypark@gmail.com">xjimmypark@gmail.com</a> まで。</p><h2>2. 端末内の情報</h2><p>ウォッチリスト、設定、通知、言語、保存した予測記録とリサーチ表示を端末に保存します。任意の資格情報はiOSキーチェーンに保存します。アカウント、証券口座接続、カード情報は不要です。</p><h2>3. ネットワークサービス</h2><p>相場、チャート、ニュース、マクロ系列にはデータ提供者とFREDへの通信が必要です。提供者は各ポリシーに従い、要求された銘柄や技術情報を受け取る場合があります。</p><h2>4. 広告と購入</h2><p>クオンタクティックPro以外ではGoogle Mobile Adsの広告が表示される場合があります。Quantactic Pro MonthlyとQuantactic Pro Annualの購入はApple StoreKitで処理され、カード番号は保存しません。米国参考価格は月額$4.99、年額$39.99です。</p><h2>5. Apple Intelligence</h2><p>対応端末ではApple IntelligenceとFoundation Modelsが端末内の説明を支援します。対応するプロンプトを第三者クラウドAIへ送信しません。</p><h2>6. 通知と削除</h2><p>通知は任意のローカル通知です。サーバーで継続的に監視することはありません。設定と履歴は変更またはアプリ削除まで端末に残ります。お問い合わせは <a href="mailto:xjimmypark@gmail.com">xjimmypark@gmail.com</a> まで。</p>''',
        "terms": '''<div class="callout"><strong>重要:</strong> クオンタクティックは情報提供・教育目的の市場分析ツールです。証券会社、投資顧問、取引プラットフォーム、推奨サービスではありません。</div><h2>1. 合意とApple標準EULA</h2><p>本規約はクオンタクティックに適用されます。アプリはApp Storeを通じてライセンスされます。<a href="https://www.apple.com/legal/internet-services/itunes/dev/stdeula/">Apple Licensed Application EULA</a>が適用されます。</p><h2>2. 情報目的のみ</h2><p>相場、チャート、ニュース、マクロ、シグナル、予測、AI回答は一般的な情報・教育目的です。個別の投資助言ではありません。取引執行、証券口座接続、入金受け入れ、資産管理は行いません。</p><h2>3. シグナルと予測</h2><ul><li>市場情報は遅延、不完全、不正確な場合があります。</li><li>シグナルは分析条件の説明であり推奨ではありません。</li><li>予測は過去の市場行動から導く確率ベースのシナリオで、価格目標、売買指示、保証ではありません。</li><li>AIの説明は独立して確認してください。</li></ul><h2>4. Quantactic Pro</h2><p><strong>Quantactic Pro Monthly</strong>は月額$4.99、<strong>Quantactic Pro Annual</strong>は年額$39.99（米国参考価格）です。両方とも同じPro機能を解放し、違いは期間と価格だけです。少なくとも24時間前に解約しない限り自動更新されます。Appleで管理し、対象時は購入を復元できます。</p><p>Proは7日予測無制限、30日・90日の確率ベースの見通し、深いモデル根拠、拡張AI、より高い上限、広告なしを提供します。</p><h2>5. 第三者サービスと連絡先</h2><p>第三者サービスには各規約が適用されます。機能とデータ源は変更または利用できない場合があります。お問い合わせは <a href="mailto:xjimmypark@gmail.com">xjimmypark@gmail.com</a> まで。</p>''',
    },
    "ko": {
        "privacy": '''<div class="callout">퀀트택틱은 계정이 필요 없는 시장 리서치 앱입니다. 설명된 범위의 리서치 기록과 AI 상호작용은 로컬로 유지되도록 설계되지만 시장·매크로 데이터, 광고, 구매 및 제3자 서비스에는 필요한 네트워크 연결이 사용됩니다.</div><h2>1. 운영 주체</h2><p>퀀트택틱은 iPhone 시장 분석 앱입니다. 문의: <a href="mailto:xjimmypark@gmail.com">xjimmypark@gmail.com</a>.</p><h2>2. 기기에 저장되는 정보</h2><p>관심종목, 설정, 알림, 언어, 저장된 전망 기록과 리서치 화면을 기기에 저장합니다. 선택한 자격 증명은 iOS 키체인에 저장합니다. 계정·증권 계좌 연결·카드 정보는 필요하지 않습니다.</p><h2>3. 네트워크 서비스</h2><p>시세, 차트, 뉴스와 매크로 시계열에는 데이터 제공자와 FRED 통신이 필요합니다. 제공자는 정책에 따라 요청한 종목과 기술 정보를 받을 수 있습니다.</p><h2>4. 광고와 구매</h2><p>퀀트택틱 Pro가 없으면 Google Mobile Ads 광고가 표시될 수 있습니다. Quantactic Pro Monthly와 Quantactic Pro Annual은 Apple StoreKit으로 처리하며 카드 번호는 저장하지 않습니다. 미국 참고 가격은 월 $4.99, 연 $39.99입니다.</p><h2>5. Apple Intelligence</h2><p>지원 기기에서는 Apple Intelligence와 Foundation Models가 기기 내 설명을 제공합니다. 지원되는 프롬프트를 제3자 클라우드 AI로 보내지 않습니다.</p><h2>6. 알림과 삭제</h2><p>알림은 선택 가능한 로컬 알림입니다. 서버에서 지속적으로 포트폴리오를 감시하지 않습니다. 설정과 기록은 변경하거나 앱을 삭제할 때까지 기기에 남습니다. 문의: <a href="mailto:xjimmypark@gmail.com">xjimmypark@gmail.com</a>.</p>''',
        "terms": '''<div class="callout"><strong>중요:</strong> 퀀트택틱은 정보·교육용 시장 분석 도구입니다. 증권사·투자자문·거래 플랫폼·추천 서비스가 아닙니다.</div><h2>1. 동의 및 Apple 표준 EULA</h2><p>본 약관은 퀀트택틱에 적용됩니다. 앱은 App Store를 통해 라이선스되며 <a href="https://www.apple.com/legal/internet-services/itunes/dev/stdeula/">Apple Licensed Application EULA</a>가 적용됩니다.</p><h2>2. 정보 목적만</h2><p>시세, 차트, 뉴스, 매크로, 시그널, 전망과 AI 응답은 일반 정보·교육 목적입니다. 맞춤 투자 자문이 아니며 거래 실행, 증권 계좌 연결, 입금 수취, 자산 관리를 하지 않습니다.</p><h2>3. 시그널과 전망</h2><ul><li>시장 정보는 지연·불완전·부정확할 수 있습니다.</li><li>시그널은 분석 조건 설명이며 추천이 아닙니다.</li><li>전망은 과거 시장 행동에서 도출한 확률 기반 시나리오이며 목표가·매매 지시·보장이 아닙니다.</li><li>AI 설명은 독립적으로 확인하세요.</li></ul><h2>4. Quantactic Pro</h2><p><strong>Quantactic Pro Monthly</strong>는 월 $4.99, <strong>Quantactic Pro Annual</strong>은 연 $39.99(미국 참고 가격)입니다. 같은 Pro 기능을 제공하며 차이는 기간과 가격뿐입니다. 기간 종료 최소 24시간 전에 취소하지 않으면 자동 갱신됩니다. Apple에서 관리하고 해당 시 구매를 복원하세요.</p><p>Pro는 7일 전망 무제한, 30·90일 전체 확률 기반 전망, 깊은 모델 근거, 확장 AI, 높은 한도와 광고 없는 경험을 제공합니다.</p><h2>5. 제3자 서비스와 문의</h2><p>제3자 서비스에는 각 약관이 적용됩니다. 기능과 데이터는 변경되거나 이용할 수 없을 수 있습니다. 문의: <a href="mailto:xjimmypark@gmail.com">xjimmypark@gmail.com</a>.</p>''',
    },
    "zh-Hans": {
        "privacy": '''<div class="callout">Quantactic 是一款无需账户的市场研究应用。说明范围内的研究历史和 AI 交互设计为保留在本地，但市场、宏观数据、广告、购买和第三方服务会按需要使用网络。</div><h2>1. 我们是谁</h2><p>Quantactic 是 iPhone 市场分析应用。隐私问题请联系 <a href="mailto:xjimmypark@gmail.com">xjimmypark@gmail.com</a>。</p><h2>2. 设备端信息</h2><p>应用在设备端保存自选、设置、通知、语言、已保存的走势预测记录与研究视图。可选凭据使用 iOS 钥匙串。无需账户，不连接券商，也不保存银行卡信息。</p><h2>3. 网络服务</h2><p>行情、图表、新闻和宏观数据需要连接数据提供方与 FRED。提供方可能按自身政策接收请求的标的和技术信息。</p><h2>4. 广告与购买</h2><p>没有 Quantactic Pro 时可能显示 Google Mobile Ads 广告。Quantactic Pro Monthly 和 Quantactic Pro Annual 由 Apple StoreKit 处理，我们不保存银行卡号。美国参考价为每月 $4.99、每年 $39.99。</p><h2>5. Apple Intelligence</h2><p>支持的设备使用 Apple Intelligence 和 Foundation Models 提供设备端解释。不会把支持的提示发送到第三方云端 AI。</p><h2>6. 通知与删除</h2><p>通知是可选的设备端通知，不代表服务器持续监控投资组合。设置和历史会保留到修改或删除应用。隐私问题请联系 <a href="mailto:xjimmypark@gmail.com">xjimmypark@gmail.com</a>。</p>''',
        "terms": '''<div class="callout"><strong>重要：</strong>Quantactic 是信息与教育用途的市场分析工具，不是券商、投资顾问、交易平台或推荐服务。</div><h2>1. 协议与 Apple 标准 EULA</h2><p>本条款适用于 Quantactic。应用通过 App Store 许可，适用 <a href="https://www.apple.com/legal/internet-services/itunes/dev/stdeula/">Apple Licensed Application EULA</a>。</p><h2>2. 仅供信息</h2><p>行情、图表、新闻、宏观、信号、走势预测与 AI 回复仅用于一般信息和教育，不构成个性化投资建议。Quantactic 不执行交易、不连接券商、不接受存款、不管理投资。</p><h2>3. 信号与走势预测</h2><ul><li>市场信息可能延迟、不完整或不准确。</li><li>信号描述分析条件，不是推荐。</li><li>走势预测是基于历史市场行为的概率型情景，不是目标价、交易指令或保证。</li><li>请独立核验 AI 解释。</li></ul><h2>4. Quantactic Pro</h2><p><strong>Quantactic Pro Monthly</strong>每月 $4.99，<strong>Quantactic Pro Annual</strong>每年 $39.99（美国参考价格）。两者提供相同的 Pro 功能，区别仅在计费周期和价格。除非至少提前 24 小时取消，否则自动续订。请在 Apple 管理订阅，并在符合条件时恢复购买。</p><p>Pro 提供无限 7 日预测、完整 30 日和 90 日概率型走势预测、更深入的模型依据、扩展设备端私密 AI、更高额度和无插页广告体验。</p><h2>5. 第三方服务与联系</h2><p>第三方服务适用其自身条款。功能和数据可能变化或不可用。条款问题请联系 <a href="mailto:xjimmypark@gmail.com">xjimmypark@gmail.com</a>。</p>''',
    },
}


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    print("wrote", path.relative_to(ROOT))


def main() -> None:
    for lang in LANGS:
        code = lang["code"]
        write(ROOT / code / "index.html", index_page(code, True))
        write(ROOT / code / "privacy.html", legal_page(code, "privacy", True))
        write(ROOT / code / "terms.html", legal_page(code, "terms", True))
    write(ROOT / "index.html", index_page("en", False))
    write(ROOT / "privacy.html", legal_page("en", "privacy", False))
    write(ROOT / "terms.html", legal_page("en", "terms", False))
    write(ROOT / "README.md", """# Quantactic Landing

Static marketing + legal site for Quantactic and App Store Connect.

Product: **Quantactic — market intelligence that shows its work.**

Locales:
- English
- Korean
- Japanese
- Simplified Chinese
- Spanish

U.S. subscription reference:
- Quantactic Pro Monthly — **$4.99/month**
- Quantactic Pro Annual — **$39.99/year** (about 33% savings)

The content dictionaries in `scripts/build_site.py` are the source of truth.

## Build

```bash
python3 scripts/build_site.py
```

## Verify

```bash
python3 scripts/verify_site.py
```

The root English aliases `/`, `/privacy.html`, and `/terms.html` remain stable for App Store Connect and GitHub Pages.
""")
    print("done")


if __name__ == "__main__":
    main()
