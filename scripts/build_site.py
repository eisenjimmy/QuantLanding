#!/usr/bin/env python3
"""Generate Quantfox landing pages for App Store Connect language URLs.

Produces:
  /index.html, /privacy.html, /terms.html   (English defaults for ASC)
  /en/, /es/, /ja/, /ko/, /zh-Hans/         (localized copies)

Run from repo root or this scripts folder:
  python3 scripts/build_site.py
"""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

LANGS = [
    {"code": "en", "html_lang": "en", "label": "English", "short": "EN"},
    {"code": "es", "html_lang": "es", "label": "Español", "short": "ES"},
    {"code": "ja", "html_lang": "ja", "label": "日本語", "short": "JA"},
    {"code": "ko", "html_lang": "ko", "label": "한국어", "short": "KO"},
    {"code": "zh-Hans", "html_lang": "zh-Hans", "label": "简体中文", "short": "中文"},
]

# ---------------------------------------------------------------------------
# Content (en source of truth, then translations)
# ---------------------------------------------------------------------------

CONTENT = {
    "en": {
        "brand": "Quantfox",
        "nav_product": "Product",
        "nav_privacy": "Privacy",
        "nav_terms": "Terms",
        "lang_label": "Language",
        "meta_index": "Quantfox is a focused market desk for iPhone with watchlists, charts, macro context, risk-aware signals, and on-device AI.",
        "title_index": "Quantfox — Market intelligence for iPhone",
        "meta_privacy": "Quantfox Privacy Policy",
        "title_privacy": "Privacy Policy — Quantfox",
        "meta_terms": "Quantfox Terms of Use",
        "title_terms": "Terms of Use — Quantfox",
        "hero_eyebrow": "MARKET INTELLIGENCE FOR IPHONE",
        "hero_h1_1": "See the market.",
        "hero_h1_2": "Test the range.",
        "hero_h1_3": "Decide with context.",
        "hero_lede": "Quantfox brings watchlists, charts, macro context, risk-aware signals, and on-device market assistance into one focused desk.",
        "cta_download": "Download on the App Store",
        "cta_explore": "Explore Quantfox ↓",
        "hero_fine": "iPhone · iOS 26 or later · No brokerage connection required",
        "hero_alt": "Quantfox Markets screen showing a focused watchlist and signal of the day",
        "metric_1_b": "Market desk",
        "metric_1_s": "Watchlist, movers, headlines, and session context",
        "metric_2_b": "Risk-aware signals",
        "metric_2_s": "Setups with stops, targets, and reward-to-risk context",
        "metric_3_b": "On-device AI",
        "metric_3_s": "Apple Intelligence support on compatible iPhone hardware",
        "sec1_h2": "A market desk that respects your attention.",
        "sec1_p": "Built for quick inspection without fake certainty, brokerage prompts, or performance theater.",
        "f1_h": "Focused market desk",
        "f1_p": "Follow the instruments that matter, then inspect price moves, market regime, movers, and relevant news in one place.",
        "f2_h": "Advanced charts",
        "f2_p": "Inspect candles, volume, moving averages, support and resistance, flexible ranges, and exact values by touch.",
        "f3_h": "Macro context",
        "f3_p": "Keep volatility, rates, oil, the U.S. dollar, economic releases, and market regime within reach.",
        "sec2_h2": "Clarity over certainty.",
        "sec2_p": "Quantfox makes uncertainty visible with explicit trade context and sampled forecast ranges.",
        "shot1": "Explore the range, not a promise",
        "shot2": "Review the setup and risk plan",
        "shot3": "Inspect every move in detail",
        "shot1_alt": "Quantfox Forecast screen with a range of sampled outcomes",
        "shot2_alt": "Quantfox Signal screen with a risk plan",
        "shot3_alt": "Quantfox Advanced Chart screen",
        "pro_eyebrow": "QUANTFOX PRO",
        "pro_h2": "Forecast and an uninterrupted desk.",
        "pro_p": "Quantfox Pro unlocks experimental sampled Forecasts (including longer horizons), removes interstitial ads, expands private AI and research limits, and covers future Pro tools with one subscription. Free includes limited 7-day forecast previews.",
        "price_month": "$4.99",
        "price_month_s": "per month · U.S.",
        "price_year": "$39.99",
        "price_year_s": "per year · U.S.",
        "notice": "<b>For information and education only.</b> Quantfox does not execute trades, connect to brokerage accounts, or provide personalized investment advice. Market data may be delayed. Forecasts, signals, and analysis are not guarantees and investing involves risk, including possible loss of principal.",
        "footer_copy": "© 2026 Quantfox. All rights reserved.",
        "footer_privacy": "Privacy Policy",
        "footer_terms": "Terms of Use",
        "footer_support": "Support",
        "legal_eyebrow": "LEGAL",
        "privacy_h1": "Privacy Policy",
        "privacy_dates": "Effective date: July 30, 2026 · Last updated: July 30, 2026",
        "terms_h1": "Terms of Use",
        "terms_dates": "Effective date: July 30, 2026 · Last updated: July 30, 2026",
        "privacy_body": """
    <div class="callout">Quantfox is designed as a no-account market-analysis app. This policy explains the information handled by the app, the services it contacts, and the choices available to you.</div>
    <h2>1. Who we are</h2><p>Quantfox is an iPhone market-analysis application. For privacy questions, contact the developer at <a href="mailto:xjimmypark@gmail.com">xjimmypark@gmail.com</a>.</p>
    <h2>2. Information stored on your device</h2><p>Quantfox stores the following information locally on your device to make the app work:</p><ul><li>Watchlist, alerts, chart preferences, notification preferences, language preference, and display settings.</li><li>Saved forecast records and selected forecast views.</li><li>Quantfox AI conversation content, when you use the AI feature.</li><li>Optional provider credentials, if you enter them for a supported integration; those credentials are stored using the iOS Keychain.</li></ul><p>Quantfox does not require an account, collect a profile, connect to a brokerage account, or store payment-card information.</p>
    <h2>3. Market data and news requests</h2><p>To show market data, charts, symbol search results, and headlines, Quantfox sends network requests to market-data providers (currently Yahoo Finance endpoints) and requests macroeconomic series from the Federal Reserve Bank of St. Louis FRED service. These requests include the market symbol or data series needed for the request. Like other internet services, those providers may receive technical information such as your IP address and device/network metadata under their own privacy practices.</p>
    <h2>4. Advertising</h2><p>Users without an active Quantfox Pro subscription may see interstitial ads served through Google Mobile Ads. Google and its advertising partners may process information associated with ad delivery, measurement, fraud prevention, and ad personalization according to their own policies and your applicable device or account settings.</p><p>Learn more in <a href="https://policies.google.com/privacy">Google’s Privacy Policy</a> and <a href="https://policies.google.com/technologies/ads">How Google uses information from sites or apps that use its services</a>.</p>
    <h2>5. Purchases</h2><p>Quantfox Pro subscriptions (monthly and annual) are processed by Apple through StoreKit and the App Store. Quantfox does not receive or store your payment-card number. Apple handles transaction records and subscription management under Apple’s privacy practices. U.S. reference prices are $4.99 per month and $39.99 per year; regional prices are shown by Apple.</p>
    <h2>6. Apple Intelligence and Quantfox AI</h2><p>On compatible devices, Quantfox AI uses Apple’s on-device Foundation Models framework. Quantfox does not send your AI prompts to a third-party cloud AI provider. Apple Intelligence availability and processing are subject to Apple’s device settings and policies. Free users have a limited daily AI question allowance; Pro unlocks expanded private AI use.</p>
    <h2>7. Notifications and sharing</h2><p>Notifications are optional and used only for market or signal alerts you enable. Quantfox uses local notifications and requests permission through iOS. If you choose to share a Quantfox image or link, iOS sends the content only to the destination you select.</p>
    <h2>8. How long information is retained</h2><p>Local preferences and locally saved content remain on your device until you change them or delete the app. Forecast records remain on device for evaluation and product history for an extended period after generation, then expire. Quantfox does not operate a user-account database for this information.</p>
    <h2>9. Your choices and deletion</h2><p>You can change notification and advertising-related device settings in iOS, manage your Quantfox Pro subscription through Apple, and remove local Quantfox data by deleting the app from your device. Because Quantfox does not maintain user accounts, there is no separate server-side account record for us to delete.</p>
    <h2>10. Children</h2><p>Quantfox is not directed to children. Do not use Quantfox if you are not old enough to consent to data processing where you live.</p>
    <h2>11. Changes to this policy</h2><p>We may update this policy as Quantfox changes. We will post the updated version on this page and revise the effective date above.</p>
    <h2>12. Contact</h2><p>For privacy questions or requests, email <a href="mailto:xjimmypark@gmail.com">xjimmypark@gmail.com</a>.</p>
""",
        "terms_body": """
    <div class="callout"><strong>Important:</strong> Quantfox is an informational market-analysis tool. It is not a broker, investment adviser, trading platform, or recommendation service.</div>
    <h2>1. Agreement and Apple’s standard EULA</h2><p>These Terms of Use govern your use of Quantfox. Quantfox is made available through the Apple App Store and is licensed, not sold. The <a href="https://www.apple.com/legal/internet-services/itunes/dev/stdeula/">Apple Licensed Application End User License Agreement</a> applies to your use of the app unless a valid custom end user license agreement supersedes it. These Terms add app-specific rules for Quantfox.</p>
    <h2>2. Eligibility and acceptable use</h2><p>You may use Quantfox only in compliance with applicable law. You may not reverse engineer, interfere with, misuse, resell, or attempt to gain unauthorized access to Quantfox, its services, or its data sources.</p>
    <h2>3. Informational use only; no investment advice</h2><p>Quotes, charts, news, macro data, signals, forecasts, and AI responses are provided for general informational and educational purposes. They are not personalized investment, legal, tax, accounting, or financial advice. They do not account for your objectives, financial situation, holdings, risk tolerance, or jurisdiction.</p><p>You are solely responsible for your investment and trading decisions. Before acting on any information, consider obtaining advice from an appropriately licensed professional.</p>
    <h2>4. Market data, signals, forecasts, and AI</h2><ul><li>Market information may be delayed, incomplete, unavailable, or inaccurate.</li><li>Signals describe analytical conditions; they are not offers, solicitations, or recommendations to buy or sell a security.</li><li>Forecasts are experimental sampled scenarios, not price targets, predictions, or guarantees. They do not incorporate every source of market risk, including news, earnings, liquidity, macro events, or unexpected developments.</li><li>Quantfox AI is a convenience feature. Review its output independently and do not rely on it as professional advice.</li></ul>
    <h2>5. Third-party services</h2><p>Quantfox may display or link to information from third-party services, including market-data, news, macroeconomic-data, advertising, Apple, and App Store services. Those services are governed by their own terms and policies. We do not control, endorse, or guarantee third-party content, availability, or accuracy.</p>
    <h2>6. Quantfox Pro subscription</h2><p>Quantfox Pro offers auto-renewable monthly and annual subscriptions currently priced at <strong>$4.99 per month</strong> or <strong>$39.99 per year</strong> in the United States, or the price shown to you in the App Store for your region. Payment is charged to your Apple ID account at confirmation of purchase. Subscriptions automatically renew unless cancelled at least 24 hours before the end of the current period. Manage or cancel in your Apple Account subscription settings. Use Restore Purchases in Quantfox when eligible.</p><p>Pro unlocks experimental Forecasts (including longer horizons), removes interstitial ads, expands private AI and research limits, and may unlock future Pro tools. Free users may run a limited number of 7-day forecast previews and may see ads.</p>
    <div class="table"><table><thead><tr><th>Subscription term</th><th>How it works</th></tr></thead><tbody><tr><td>Payment</td><td>Charged to your Apple Account when you confirm purchase.</td></tr><tr><td>Renewal</td><td>Renews automatically unless cancelled at least 24 hours before the end of the current period.</td></tr><tr><td>Management</td><td>Manage or cancel through your Apple Account subscription settings.</td></tr><tr><td>Restore</td><td>Use Restore Purchases in Quantfox when eligible.</td></tr><tr><td>U.S. price reference</td><td>$4.99 / month or $39.99 / year (regional pricing may differ).</td></tr></tbody></table></div>
    <h2>7. Intellectual property</h2><p>Quantfox, its design, software, and original content are protected by applicable intellectual-property laws. Third-party names, logos, data, and content remain the property of their respective owners.</p>
    <h2>8. Availability and changes</h2><p>We may change, suspend, or discontinue features, data sources, subscriptions, or access to Quantfox at any time. We do not guarantee uninterrupted, error-free, timely, or secure operation.</p>
    <h2>9. Disclaimer of warranties</h2><p>To the maximum extent permitted by law, Quantfox is provided on an “as is” and “as available” basis without warranties of any kind, whether express, implied, or statutory, including warranties of accuracy, fitness for a particular purpose, merchantability, and non-infringement.</p>
    <h2>10. Limitation of liability</h2><p>To the maximum extent permitted by law, Quantfox and its developer will not be liable for indirect, incidental, special, consequential, exemplary, or punitive damages, or for lost profits, lost data, trading losses, or business interruption arising from or related to Quantfox or its content.</p>
    <h2>11. Changes to these terms</h2><p>We may update these Terms as Quantfox changes. The updated version will be posted here with a revised effective date. Your continued use after an update means you accept the updated Terms to the extent permitted by law.</p>
    <h2>12. Contact</h2><p>For questions about these Terms, email <a href="mailto:xjimmypark@gmail.com">xjimmypark@gmail.com</a>. See the <a href="privacy.html">Privacy Policy</a> for information about data handling.</p>
""",
    }
}

# Spanish
CONTENT["es"] = {
    **CONTENT["en"],
    "nav_product": "Producto",
    "nav_privacy": "Privacidad",
    "nav_terms": "Términos",
    "lang_label": "Idioma",
    "meta_index": "Quantfox es un escritorio de mercado para iPhone con listas de seguimiento, gráficos, macro, señales y IA en el dispositivo.",
    "title_index": "Quantfox — Inteligencia de mercado para iPhone",
    "meta_privacy": "Política de privacidad de Quantfox",
    "title_privacy": "Política de privacidad — Quantfox",
    "meta_terms": "Términos de uso de Quantfox",
    "title_terms": "Términos de uso — Quantfox",
    "hero_eyebrow": "INTELIGENCIA DE MERCADO PARA IPHONE",
    "hero_h1_1": "Mira el mercado.",
    "hero_h1_2": "Prueba el rango.",
    "hero_h1_3": "Decide con contexto.",
    "hero_lede": "Quantfox reúne listas de seguimiento, gráficos, contexto macro, señales con gestión de riesgo y asistencia de mercado en el dispositivo en un solo escritorio.",
    "cta_download": "Descargar en el App Store",
    "cta_explore": "Explorar Quantfox ↓",
    "hero_fine": "iPhone · iOS 26 o posterior · Sin conexión a bróker",
    "hero_alt": "Pantalla Markets de Quantfox con lista de seguimiento y señal del día",
    "metric_1_b": "Escritorio de mercado",
    "metric_1_s": "Lista, movers, titulares y contexto de sesión",
    "metric_2_b": "Señales con riesgo",
    "metric_2_s": "Setups con stops, objetivos y recompensa/riesgo",
    "metric_3_b": "IA en el dispositivo",
    "metric_3_s": "Apple Intelligence en hardware compatible",
    "sec1_h2": "Un escritorio de mercado que respeta tu atención.",
    "sec1_p": "Hecho para inspeccionar rápido, sin certeza falsa ni promesas de bróker.",
    "f1_h": "Escritorio enfocado",
    "f1_p": "Sigue los instrumentos que importan e inspecciona precio, régimen, movers y noticias en un solo lugar.",
    "f2_h": "Gráficos avanzados",
    "f2_p": "Velas, volumen, medias móviles, soporte y resistencia, rangos flexibles y valores exactos al tacto.",
    "f3_h": "Contexto macro",
    "f3_p": "Volatilidad, tipos, petróleo, dólar, datos y régimen de mercado al alcance.",
    "sec2_h2": "Claridad antes que certeza.",
    "sec2_p": "Quantfox hace visible la incertidumbre con contexto de operación y rangos de forecast muestreados.",
    "shot1": "Explora el rango, no una promesa",
    "shot2": "Revisa el setup y el plan de riesgo",
    "shot3": "Inspecciona cada movimiento",
    "pro_eyebrow": "QUANTFOX PRO",
    "pro_h2": "Forecast y un escritorio sin interrupciones.",
    "pro_p": "Quantfox Pro desbloquea Forecasts experimentales (incluidos horizontes largos), quita anuncios intersticiales, amplía la IA privada y los límites de investigación, y cubre futuras herramientas Pro con una suscripción. La versión gratuita incluye vistas previas limitadas de forecast a 7 días.",
    "price_month_s": "al mes · EE. UU.",
    "price_year_s": "al año · EE. UU.",
    "notice": "<b>Solo información y educación.</b> Quantfox no ejecuta operaciones, no se conecta a brókers ni ofrece asesoramiento de inversión personalizado. Los datos pueden retrasarse. Forecasts, señales y análisis no son garantías; invertir implica riesgo, incluida la pérdida de capital.",
    "footer_copy": "© 2026 Quantfox. Todos los derechos reservados.",
    "footer_privacy": "Política de privacidad",
    "footer_terms": "Términos de uso",
    "footer_support": "Soporte",
    "privacy_h1": "Política de privacidad",
    "privacy_dates": "Fecha de vigencia: 30 de julio de 2026 · Actualizada: 30 de julio de 2026",
    "terms_h1": "Términos de uso",
    "terms_dates": "Fecha de vigencia: 30 de julio de 2026 · Actualizada: 30 de julio de 2026",
    "privacy_body": CONTENT["en"]["privacy_body"]
    .replace("Quantfox is designed", "Quantfox está diseñado")
    .replace("This policy explains", "Esta política explica")
    .replace("Who we are", "Quiénes somos")
    .replace("Information stored on your device", "Información almacenada en tu dispositivo")
    .replace("Market data and news requests", "Datos de mercado y noticias")
    .replace("Advertising", "Publicidad")
    .replace("Purchases", "Compras")
    .replace("Apple Intelligence and Quantfox AI", "Apple Intelligence e IA de Quantfox")
    .replace("Notifications and sharing", "Notificaciones y compartir")
    .replace("How long information is retained", "Cuánto tiempo se conserva la información")
    .replace("Your choices and deletion", "Tus opciones y eliminación")
    .replace("Children", "Menores")
    .replace("Changes to this policy", "Cambios a esta política")
    .replace("Contact", "Contacto"),
    "terms_body": CONTENT["en"]["terms_body"]
    .replace("Important:", "Importante:")
    .replace("Agreement and Apple’s standard EULA", "Acuerdo y EULA estándar de Apple")
    .replace("Eligibility and acceptable use", "Elegibilidad y uso aceptable")
    .replace("Informational use only; no investment advice", "Solo uso informativo; sin asesoramiento de inversión")
    .replace("Market data, signals, forecasts, and AI", "Datos de mercado, señales, forecasts e IA")
    .replace("Third-party services", "Servicios de terceros")
    .replace("Quantfox Pro subscription", "Suscripción Quantfox Pro")
    .replace("Intellectual property", "Propiedad intelectual")
    .replace("Availability and changes", "Disponibilidad y cambios")
    .replace("Disclaimer of warranties", "Exención de garantías")
    .replace("Limitation of liability", "Limitación de responsabilidad")
    .replace("Changes to these terms", "Cambios a estos términos")
    .replace(">Contact<", ">Contacto<"),
}

# Japanese
CONTENT["ja"] = {
    **CONTENT["en"],
    "nav_product": "製品",
    "nav_privacy": "プライバシー",
    "nav_terms": "利用規約",
    "lang_label": "言語",
    "meta_index": "Quantfoxは、ウォッチリスト、チャート、マクロ、シグナル、オンデバイスAIを備えたiPhone向け市場デスクです。",
    "title_index": "Quantfox — iPhoneの市場インテリジェンス",
    "meta_privacy": "Quantfox プライバシーポリシー",
    "title_privacy": "プライバシーポリシー — Quantfox",
    "meta_terms": "Quantfox 利用規約",
    "title_terms": "利用規約 — Quantfox",
    "hero_eyebrow": "IPHONE向け市場インテリジェンス",
    "hero_h1_1": "市場を見る。",
    "hero_h1_2": "レンジを試す。",
    "hero_h1_3": "文脈で決める。",
    "hero_lede": "Quantfoxはウォッチリスト、チャート、マクロ、リスク認識シグナル、オンデバイス支援を一つのデスクにまとめます。",
    "cta_download": "App Storeでダウンロード",
    "cta_explore": "Quantfoxを見る ↓",
    "hero_fine": "iPhone · iOS 26以降 · 証券口座接続なし",
    "metric_1_b": "市場デスク",
    "metric_1_s": "ウォッチリスト、movers、ヘッドライン、セッション",
    "metric_2_b": "リスク認識シグナル",
    "metric_2_s": "ストップ、ターゲット、リスクリワード付き",
    "metric_3_b": "オンデバイスAI",
    "metric_3_s": "対応機種でApple Intelligence",
    "sec1_h2": "注意を尊重する市場デスク。",
    "sec1_p": "偽の確度やブローカー誘導なしで素早く確認できます。",
    "f1_h": "集中デスク",
    "f1_p": "重要な銘柄を追い、価格・レジーム・movers・ニュースを一か所で確認。",
    "f2_h": "高度なチャート",
    "f2_p": "ローソク足、出来高、移動平均、サポレジ、柔軟な期間、タッチで正確な値。",
    "f3_h": "マクロ文脈",
    "f3_p": "ボラティリティ、金利、原油、ドル、指標、市場レジームを手元に。",
    "sec2_h2": "確度より明瞭さ。",
    "sec2_p": "トレード文脈とサンプルforecastレンジで不確実性を可視化します。",
    "shot1": "約束ではなくレンジを探る",
    "shot2": "セットアップとリスク計画を確認",
    "shot3": "動きを詳細に検査",
    "pro_h2": "Forecastと途切れないデスク。",
    "pro_p": "Quantfox Proは実験的なサンプルForecast（より長いホライズン含む）を解放し、インタースティシャル広告を削除し、プライベートAIと調査上限を拡張し、将来のPro機能を一つのサブスクリプションでカバーします。無料版には限定の7日Forecastプレビューがあります。",
    "price_month_s": "月額 · 米国",
    "price_year_s": "年額 · 米国",
    "notice": "<b>情報・教育のみ。</b> Quantfoxは約定せず、証券口座に接続せず、個別の投資助言を行いません。データは遅延する場合があります。Forecast・シグナル・分析は保証ではなく、投資には元本損失を含むリスクがあります。",
    "footer_copy": "© 2026 Quantfox. All rights reserved.",
    "footer_privacy": "プライバシーポリシー",
    "footer_terms": "利用規約",
    "footer_support": "サポート",
    "privacy_h1": "プライバシーポリシー",
    "privacy_dates": "施行日: 2026年7月30日 · 最終更新: 2026年7月30日",
    "terms_h1": "利用規約",
    "terms_dates": "施行日: 2026年7月30日 · 最終更新: 2026年7月30日",
}

# Korean
CONTENT["ko"] = {
    **CONTENT["en"],
    "nav_product": "제품",
    "nav_privacy": "개인정보",
    "nav_terms": "이용약관",
    "lang_label": "언어",
    "meta_index": "Quantfox는 워치리스트, 차트, 매크로, 시그널, 온디바이스 AI를 담은 iPhone 시장 데스크입니다.",
    "title_index": "Quantfox — iPhone용 시장 인텔리전스",
    "meta_privacy": "Quantfox 개인정보 처리방침",
    "title_privacy": "개인정보 처리방침 — Quantfox",
    "meta_terms": "Quantfox 이용약관",
    "title_terms": "이용약관 — Quantfox",
    "hero_eyebrow": "아이폰을 위한 시장 인텔리전스",
    "hero_h1_1": "시장을 보고.",
    "hero_h1_2": "범위를 시험하고.",
    "hero_h1_3": "맥락으로 결정하세요.",
    "hero_lede": "Quantfox는 워치리스트, 차트, 매크로 맥락, 리스크 인식 시그널, 온디바이스 시장 지원을 하나의 데스크에 모읍니다.",
    "cta_download": "App Store에서 다운로드",
    "cta_explore": "Quantfox 살펴보기 ↓",
    "hero_fine": "iPhone · iOS 26 이상 · 증권 계좌 연결 없음",
    "metric_1_b": "시장 데스크",
    "metric_1_s": "워치리스트, 모멘텀, 헤드라인, 세션 맥락",
    "metric_2_b": "리스크 인식 시그널",
    "metric_2_s": "스탑, 목표, 손익비 포함 셋업",
    "metric_3_b": "온디바이스 AI",
    "metric_3_s": "지원 기기에서 Apple Intelligence",
    "sec1_h2": "주의를 존중하는 시장 데스크.",
    "sec1_p": "가짜 확신이나 브로커 유도 없이 빠르게 점검하도록 설계했습니다.",
    "f1_h": "집중 데스크",
    "f1_p": "중요한 종목을 따라가며 가격, 레짐, 모멘텀, 뉴스를 한곳에서 확인하세요.",
    "f2_h": "고급 차트",
    "f2_p": "캔들, 거래량, 이동평균, 지지·저항, 유연한 기간, 터치로 정확한 값.",
    "f3_h": "매크로 맥락",
    "f3_p": "변동성, 금리, 원유, 달러, 경제 지표, 시장 레짐을 가까이.",
    "sec2_h2": "확실성보다 명확함.",
    "sec2_p": "트레이드 맥락과 샘플 forecast 범위로 불확실성을 드러냅니다.",
    "shot1": "약속이 아니라 범위를 탐색",
    "shot2": "셋업과 리스크 플랜 검토",
    "shot3": "모든 움직임을 자세히 검사",
    "pro_h2": "Forecast와 끊김 없는 데스크.",
    "pro_p": "Quantfox Pro는 실험적 샘플 Forecast(더 긴 기간 포함)를 잠금 해제하고, 전면 광고를 제거하며, 프라이빗 AI·리서치 한도를 확장하고, 향후 Pro 도구를 하나의 구독으로 포함합니다. 무료는 제한된 7일 Forecast 미리보기를 제공합니다.",
    "price_month_s": "월 · 미국",
    "price_year_s": "년 · 미국",
    "notice": "<b>정보·교육 목적만.</b> Quantfox는 주문을 실행하지 않고, 증권 계좌에 연결하지 않으며, 맞춤 투자 자문을 제공하지 않습니다. 시세는 지연될 수 있습니다. Forecast·시그널·분석은 보장이 아니며 투자에는 원금 손실 위험이 있습니다.",
    "footer_copy": "© 2026 Quantfox. All rights reserved.",
    "footer_privacy": "개인정보 처리방침",
    "footer_terms": "이용약관",
    "footer_support": "지원",
    "privacy_h1": "개인정보 처리방침",
    "privacy_dates": "시행일: 2026년 7월 30일 · 최종 업데이트: 2026년 7월 30일",
    "terms_h1": "이용약관",
    "terms_dates": "시행일: 2026년 7월 30일 · 최종 업데이트: 2026년 7월 30일",
}

# Simplified Chinese
CONTENT["zh-Hans"] = {
    **CONTENT["en"],
    "nav_product": "产品",
    "nav_privacy": "隐私",
    "nav_terms": "条款",
    "lang_label": "语言",
    "meta_index": "Quantfox 是面向 iPhone 的市场工作台，包含自选、图表、宏观、信号与设备端 AI。",
    "title_index": "Quantfox — iPhone 市场情报",
    "meta_privacy": "Quantfox 隐私政策",
    "title_privacy": "隐私政策 — Quantfox",
    "meta_terms": "Quantfox 使用条款",
    "title_terms": "使用条款 — Quantfox",
    "hero_eyebrow": "面向 IPHONE 的市场情报",
    "hero_h1_1": "看见市场。",
    "hero_h1_2": "试探区间。",
    "hero_h1_3": "带着上下文决策。",
    "hero_lede": "Quantfox 将自选、图表、宏观、风险感知信号与设备端市场辅助整合到一个专注工作台。",
    "cta_download": "在 App Store 下载",
    "cta_explore": "探索 Quantfox ↓",
    "hero_fine": "iPhone · iOS 26 或更高 · 无需券商连接",
    "metric_1_b": "市场工作台",
    "metric_1_s": "自选、异动、头条与时段上下文",
    "metric_2_b": "风险感知信号",
    "metric_2_s": "含止损、目标与盈亏比的设置",
    "metric_3_b": "设备端 AI",
    "metric_3_s": "兼容机型上的 Apple Intelligence",
    "sec1_h2": "尊重注意力的市场工作台。",
    "sec1_p": "为快速检查而建，没有虚假确定性或券商推销。",
    "f1_h": "专注工作台",
    "f1_p": "跟踪重要标的，在一处查看价格、体制、异动与相关新闻。",
    "f2_h": "高级图表",
    "f2_p": "K 线、成交量、均线、支撑阻力、灵活周期与触控精确读数。",
    "f3_h": "宏观上下文",
    "f3_p": "波动、利率、原油、美元、经济数据与市场体制触手可及。",
    "sec2_h2": "清晰先于确定。",
    "sec2_p": "用交易上下文与采样 forecast 区间让不确定性可见。",
    "shot1": "探索区间，而非承诺",
    "shot2": "查看设置与风险计划",
    "shot3": "仔细检查每一处波动",
    "pro_h2": "Forecast 与不间断的工作台。",
    "pro_p": "Quantfox Pro 解锁实验性采样 Forecast（含更长周期）、移除插页广告、扩展私密 AI 与研究额度，并以单一订阅覆盖未来 Pro 工具。免费版包含有限的 7 日 Forecast 预览。",
    "price_month_s": "每月 · 美国",
    "price_year_s": "每年 · 美国",
    "notice": "<b>仅供信息与教育。</b> Quantfox 不执行交易、不连接券商账户、不提供个性化投资建议。行情可能延迟。Forecast、信号与分析不是保证；投资有风险，包括本金损失。",
    "footer_copy": "© 2026 Quantfox. 保留所有权利。",
    "footer_privacy": "隐私政策",
    "footer_terms": "使用条款",
    "footer_support": "支持",
    "privacy_h1": "隐私政策",
    "privacy_dates": "生效日期：2026 年 7 月 30 日 · 最后更新：2026 年 7 月 30 日",
    "terms_h1": "使用条款",
    "terms_dates": "生效日期：2026 年 7 月 30 日 · 最后更新：2026 年 7 月 30 日",
}


def asset_prefix(in_locale_folder: bool) -> str:
    return "../" if in_locale_folder else ""


def lang_switcher(current: str, page: str, in_locale_folder: bool) -> str:
    """page is index|privacy|terms"""
    file = "index.html" if page == "index" else f"{page}.html"
    items = []
    for lang in LANGS:
        code = lang["code"]
        if in_locale_folder:
            href = f"../{code}/{file}" if code != current else file
        else:
            href = f"{code}/{file}"
        current_attr = ' aria-current="true"' if code == current else ""
        items.append(
            f'<a href="{href}" hreflang="{lang["html_lang"]}"{current_attr}>{lang["label"]}</a>'
        )
    current_label = next(l["short"] for l in LANGS if l["code"] == current)
    menu = "\n          ".join(items)
    return f"""<details class="lang-switch">
        <summary aria-label="Language">{current_label}</summary>
        <div class="lang-menu" role="menu">
          {menu}
        </div>
      </details>"""


def nav(c: dict, current: str, page: str, in_locale_folder: bool) -> str:
    p = asset_prefix(in_locale_folder)
    home = "index.html"
    privacy = "privacy.html"
    terms = "terms.html"
    product_href = "#product" if page == "index" else home + "#product"
    return f"""<nav class="nav" aria-label="Primary navigation">
      <a class="brand" href="{home}" aria-label="{c['brand']} home"><span class="mark"><img src="{p}assets/quant-app-icon.png" alt=""></span>{c['brand']}</a>
      <div class="nav-right">
        <div class="nav-links"><a href="{product_href}">{c['nav_product']}</a><a href="{privacy}">{c['nav_privacy']}</a><a href="{terms}">{c['nav_terms']}</a></div>
        {lang_switcher(current, page, in_locale_folder)}
      </div>
    </nav>"""


def head(c: dict, title: str, description: str, in_locale_folder: bool, page: str, lang_code: str) -> str:
    p = asset_prefix(in_locale_folder)
    html_lang = next(l["html_lang"] for l in LANGS if l["code"] == lang_code)
    alts = []
    for lang in LANGS:
        if in_locale_folder:
            href = f"../{lang['code']}/{page if page != 'index' else 'index'}.html"
        else:
            href = f"{lang['code']}/{page if page != 'index' else 'index'}.html"
        if page == "index":
            file = "index.html"
        else:
            file = f"{page}.html"
        if in_locale_folder:
            href = f"../{lang['code']}/{file}"
        else:
            href = f"{lang['code']}/{file}"
        alts.append(f'  <link rel="alternate" hreflang="{lang["html_lang"]}" href="{href}">')
    alts.append(f'  <link rel="alternate" hreflang="x-default" href="{"en/" if not in_locale_folder else "../en/"}{ "index.html" if page == "index" else page + ".html" }">')
    return f"""<!doctype html>
<html lang="{html_lang}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="{description}">
  <title>{title}</title>
  <link rel="stylesheet" href="{p}css/site.css">
{chr(10).join(alts)}
</head>
<body>
"""


def index_page(lang_code: str, in_locale_folder: bool) -> str:
    c = CONTENT[lang_code]
    p = asset_prefix(in_locale_folder)
    return (
        head(c, c["title_index"], c["meta_index"], in_locale_folder, "index", lang_code)
        + f"""  <div class="shell">
    {nav(c, lang_code, "index", in_locale_folder)}
    <main>
      <section class="hero">
        <div>
          <div class="eyebrow"><span class="dot"></span>{c["hero_eyebrow"]}</div>
          <h1>{c["hero_h1_1"]}<br><em>{c["hero_h1_2"]}</em><br>{c["hero_h1_3"]}</h1>
          <p class="lede">{c["hero_lede"]}</p>
          <div class="actions"><a class="button" href="https://apps.apple.com/us/search?term=Quantfox">{c["cta_download"]}</a><a class="text-link" href="#product">{c["cta_explore"]}</a></div>
          <p class="fine">{c["hero_fine"]}</p>
        </div>
        <div class="hero-shot"><img src="{p}assets/01-your-market-distilled.png" alt="{c["hero_alt"]}"></div>
      </section>
    </main>
  </div>

  <section class="strip" aria-label="Quantfox overview"><div class="shell strip-inner"><div class="metric"><b>{c["metric_1_b"]}</b><span>{c["metric_1_s"]}</span></div><div class="metric"><b>{c["metric_2_b"]}</b><span>{c["metric_2_s"]}</span></div><div class="metric"><b>{c["metric_3_b"]}</b><span>{c["metric_3_s"]}</span></div></div></section>

  <main class="shell">
    <section class="section" id="product">
      <div class="section-heading"><h2>{c["sec1_h2"]}</h2><p>{c["sec1_p"]}</p></div>
      <div class="feature-grid">
        <article class="feature"><div class="icon">⌁</div><h3>{c["f1_h"]}</h3><p>{c["f1_p"]}</p></article>
        <article class="feature"><div class="icon">↗</div><h3>{c["f2_h"]}</h3><p>{c["f2_p"]}</p></article>
        <article class="feature"><div class="icon">◌</div><h3>{c["f3_h"]}</h3><p>{c["f3_p"]}</p></article>
      </div>
    </section>

    <section class="section">
      <div class="section-heading"><h2>{c["sec2_h2"]}</h2><p>{c["sec2_p"]}</p></div>
      <div class="shots">
        <article class="shot"><img src="{p}assets/02-forecast-the-range.png" alt="{c["shot1_alt"]}"><div>{c["shot1"]}</div></article>
        <article class="shot"><img src="{p}assets/03-signals-with-risk-plan.png" alt="{c["shot2_alt"]}"><div>{c["shot2"]}</div></article>
        <article class="shot"><img src="{p}assets/04-inspect-every-move.png" alt="{c["shot3_alt"]}"><div>{c["shot3"]}</div></article>
      </div>
    </section>

    <section class="section"><div class="pro"><div><div class="eyebrow">{c["pro_eyebrow"]}</div><h2>{c["pro_h2"]}</h2><p>{c["pro_p"]}</p></div><div class="price-block"><div class="price">{c["price_month"]}<span>{c["price_month_s"]}</span></div><div class="price">{c["price_year"]}<span>{c["price_year_s"]}</span></div></div></div></section>

    <aside class="notice">{c["notice"]}</aside>
  </main>

  <footer><div class="shell footer-row"><span>{c["footer_copy"]}</span><span class="footer-links"><a href="privacy.html">{c["footer_privacy"]}</a><a href="terms.html">{c["footer_terms"]}</a><a href="mailto:xjimmypark@gmail.com">{c["footer_support"]}</a></span></div></footer>
</body>
</html>
"""
    )


def legal_page(lang_code: str, kind: str, in_locale_folder: bool) -> str:
    c = CONTENT[lang_code]
    is_privacy = kind == "privacy"
    title = c["title_privacy"] if is_privacy else c["title_terms"]
    meta = c["meta_privacy"] if is_privacy else c["meta_terms"]
    h1 = c["privacy_h1"] if is_privacy else c["terms_h1"]
    dates = c["privacy_dates"] if is_privacy else c["terms_dates"]
    body = c["privacy_body"] if is_privacy else c["terms_body"]
    other = "terms.html" if is_privacy else "privacy.html"
    other_label = c["footer_terms"] if is_privacy else c["footer_privacy"]
    return (
        head(c, title, meta, in_locale_folder, kind, lang_code)
        + f"""  <div class="shell legal">
    {nav(c, lang_code, kind, in_locale_folder)}
    <header class="legal-hero"><div class="eyebrow">{c["legal_eyebrow"]}</div><h1>{h1}</h1><p>{dates}</p></header>
    <article class="legal">
{body}
    </article>
    <footer class="legal-footer">© 2026 Quantfox · <a class="link" href="index.html">{c["nav_product"]}</a> · <a class="link" href="{other}">{other_label}</a></footer>
  </div>
</body>
</html>
"""
    )



# Load full legal bodies from scripts/legal/*.html when present
_legal_dir = Path(__file__).resolve().parent / "legal"
for _code in ("es", "ja", "ko", "zh-Hans"):
    for _kind, _key in (("privacy", "privacy_body"), ("terms", "terms_body")):
        _f = _legal_dir / f"{_code}_{_kind}.html"
        if _f.exists() and _code in CONTENT:
            CONTENT[_code][_key] = "\n    " + _f.read_text(encoding="utf-8").strip() + "\n"


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    print("wrote", path.relative_to(ROOT))


def main() -> None:
    # Locale folders
    for lang in LANGS:
        code = lang["code"]
        write(ROOT / code / "index.html", index_page(code, True))
        write(ROOT / code / "privacy.html", legal_page(code, "privacy", True))
        write(ROOT / code / "terms.html", legal_page(code, "terms", True))

    # Root English defaults for App Store Connect stable URLs
    write(ROOT / "index.html", index_page("en", False))
    write(ROOT / "privacy.html", legal_page("en", "privacy", False))
    write(ROOT / "terms.html", legal_page("en", "terms", False))

    # README for deploy / ASC
    write(
        ROOT / "README.md",
        """# Quantfox Landing

Static marketing + legal site for App Store Connect.

## URLs (GitHub Pages style)

| Language | Product | Privacy | Terms |
|---|---|---|---|
| English (default ASC) | `/` or `/en/` | `/privacy.html` or `/en/privacy.html` | `/terms.html` or `/en/terms.html` |
| Spanish | `/es/` | `/es/privacy.html` | `/es/terms.html` |
| Japanese | `/ja/` | `/ja/privacy.html` | `/ja/terms.html` |
| Korean | `/ko/` | `/ko/privacy.html` | `/ko/terms.html` |
| Simplified Chinese | `/zh-Hans/` | `/zh-Hans/privacy.html` | `/zh-Hans/terms.html` |

## Pricing (U.S. reference)

- Quantfox Pro Monthly: **$4.99**
- Quantfox Pro Annually: **$39.99**

## Rebuild after content edits

```bash
python3 scripts/build_site.py
```

Edit `scripts/build_site.py` `CONTENT` dict, then regenerate.
""",
    )
    print("done")


if __name__ == "__main__":
    main()
