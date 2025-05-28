with ordered_data as (
  select
    *,
    price * quantity as total_amount,
    row_number() over (partition by orderid order by orderid) as rn
  from
    {{ source('raw', 'orders') }}
  where
    orderid is not null
    and customername is not null
    and price >= 0
)


select
  orderid,
  customername,
  product,
  cast(quantity as integer) as quantity,
  cast(price as float) as price,
  cast(total_amount as float) as total_amount,
  cast(orderdate as date) as orderdate,
  shippedregion,
  orderstatus
from
  ordered_data
where
  rn = 1
