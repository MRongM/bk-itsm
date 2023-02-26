service = Service.objects.get(pk=15)
service.workflow.states
http://localhost:8004/api/ticket/receipts/export_group_by_service/?page_size=10&page=1&ordering=-create_at&is_draft=0&
view_type=&export_fields=sn,title,bk_biz_id,service_type_name,catalog_fullname,current_status_display,current_steps,creator,create_at,end_at,service_name,stars,
comment&service_id__in=15&service_fields=eyIxNSI6WyJ0aXRsZSJdfQ==
