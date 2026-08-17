# Quote field map

讀取報價或市場頁時，依下列順序回報，並只使用當次畫面取得的值：

1. **Identity**：頁面標題、標的名稱、代號、交易所／市場。
2. **Quote**：價格、漲跌、漲跌幅、報價時間、貨幣與盤中／休市狀態。
3. **Chart state**：目前圖表類型、時間窗、是否套用比較或技術指標。
4. **Context**：總覽頁的開高低、52 週高低、成交量、相關資產與新聞；把 AI 摘要及第三方來源分開標示。
5. **Verification**：目前 URL、頁面 title、selected tab、候選選項是否明確選取。

## Common route patterns

- Homepage: `https://www.google.com/finance/beta`
- Quote: `/finance/beta/quote/{symbol}:{exchange}`
- Chart window: quote route with a `window` query such as `window=1Y`.
- Quote sections: visible tabs `總覽`、`分析`、`收益`、`財務`、`持有資產`；實際 query state 以當次 URL 為準。

Do not assume every symbol has every quote section. Index pages may only expose `總覽`, while stock pages can expose analyst, earnings, financial, and holdings sections.
