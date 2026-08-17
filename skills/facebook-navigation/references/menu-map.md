# Facebook Navigation Menu Map

Load this reference when the visible top navigation or account menu is insufficient to choose a route. Treat labels and descriptions as UI-verified at exploration time and re-check them before use.

## Top navigation

| Label | Capability | Next route |
| --- | --- | --- |
| `首頁` | Feed and stories | `/` |
| `Marketplace` | Marketplace discovery | `/marketplace/` |
| `社團` | Group feed, discovery and joined groups | `/groups/` |
| `遊戲` | Games hub | `/gaming/play/` |

## Facebook 功能表 categories observed

- `專業`: Meta Business Suite and professional dashboard.
- `社交`: events, friends, groups, feed and pages.
- `娛樂`: gaming video and play games.
- `購物`: orders/payments and Marketplace.
- `個人`: ad activity, memories and saved items.
- `更多 Meta 產品`: Meta AI, Messenger Kids, Threads, WhatsApp and Instagram.

## Account and support menus observed

- `設定和隱私`: settings, language, privacy checkup, privacy center, activity log and content preferences.
- `協助和支援`: help, scam prevention center, account status, support inbox and report problem.
- `顯示方式和無障礙環境`: display/accessibility controls.
- `登出`: session-ending action; never activate during discovery.

Do not persist the current profile names, switchable profile names, group names or personalized menu suggestions.
