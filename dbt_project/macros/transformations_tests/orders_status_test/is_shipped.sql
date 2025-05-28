{% test is_shipped(model) %}
  SELECT *
  FROM {{ model }}
  WHERE orderstatus != 'Shipped'
{% endtest %}
