{% test is_date(model, column_name) %}
select *
from {{ model }}
where try_cast({{ column_name }} as date) is null
  and {{ column_name }} is not null
{% endtest %}
