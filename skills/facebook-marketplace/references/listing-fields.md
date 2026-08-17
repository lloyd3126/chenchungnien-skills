# Marketplace Listing Fields and Controls

## Result card

A listing card can expose a title, price or free marker, location, a recently-listed marker and a link to `/marketplace/item/<listing-id>/`. These values are current listing data and must be re-fetched for each task.

## Search and filter controls

- `搜尋 Marketplace`: keyword search.
- Location／distance button: current area and radius; values are session-dependent.
- `所有類別`: category entry on the Marketplace home.
- `篩選條件`: opens sort, price range, condition, listing date and inventory controls.
- `通知我`: notification subscription boundary; do not activate during read-only discovery.

## Detail view

The detail viewer can expose title, price, availability, seller, condition, description, approximate location and map controls. It can also expose a seller-message textbox and buttons for send, save, share and more options. Treat those controls as side-effecting even when the detail viewer opens as a dialog.

## Verification

Confirm the detail heading plus at least one of price, availability, condition or location. Never infer seller reliability, listing legitimacy, inventory or price stability from the UI alone.
