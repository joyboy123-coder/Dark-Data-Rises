{% test is_cancelled(model) %}
  SELECT *
  FROM {{ model }}
  WHERE orderstatus != 'Cancelled'
{% endtest %}
