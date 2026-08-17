# vocus Product Pages

## Product listing

The `/product` page was observed with `精選商品` and `全部商品` sections, category labels, and a sort control whose visible value was `最新上架`. A product card can expose a title, current/original price, seller salon, rating, sales/view metadata, and a detail link.

## Product detail

The observed detail route pattern is `/salon/<slug>/products/<product-id>`. Before summarizing a detail page, verify its title, seller salon, visible description, current access/purchase state, and any price/discount labels. Treat seller copy, reviews, sales, views, and availability as dynamic page content.

## Purchase boundary

Opening a public listing or detail card is read-only. Purchase, checkout, sponsorship, payment, sign-in, and external links are separate side-effect or privacy boundaries. Do not activate them during discovery, and do not enter contact or payment information.
