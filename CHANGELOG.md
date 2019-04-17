Publish History
--------
- 20180214 
    - \+ ShopeePartnerAPI main function building.  
- 20180714 
    - \+ Add new class method - shop    
      This class can get information or update information of shop ,and get shop performance includes the indexes from "My Performance" of Seller Center.
- 20180915
    - \+ Add item batch update
    - \- Rename product module to item module
    - \- Combine variation module into item module
    - \+ Create new Image module
    - \+ Create new Discount module
    - \+ Create new ShopCategory module

- 20181010
    - \+ Create new authorize module

- 20181201
    - \+ Add payment.GetPaymentList
    - \+ Add 2-Tier Variation API set 

- 20181214
    - \+ Add item.UnlistItem
    - \+ Add item.UpdateImg
    - \+ Add Top Picks Collection API set
  
- 20190130 New API Release (TBA)


- 20190225 New Handling For Partial Result Failure of Batch Type API


    ##### Please note starting from Apr 1st, 2019, ShopeeAPI will have new success/failure return rules for the below four APIs:
    - shop_category.AddItems

    - shop_category.DeleteItems

    - top_picks.AddTopPicks

    - top_picks.UpdateTopPicks

    ##### Original rule:

    ##### These APIs return failure with error code if any part of the batch failed.

    ##### New rule:

    ##### These APIs will return success code 200 as long as there is one item_id succeeds from the batch, with the following new return parameter to indicate which parts succeed or fail:


- 20190313 New Features - Edit Shop Level Logistics (TBA)
  - New API: logistics.UpdateShopLogistics
