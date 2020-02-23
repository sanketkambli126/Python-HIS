from django.contrib import admin
from .models import Hospital,Company,Member,Plans,Policy,Treatment,ClaimSettlementinfo,Claim,Benifits,Role

# Register your models here.
admin.site.register(Hospital)
admin.site.register(Company)
admin.site.register(Member)
admin.site.register(Plans)
admin.site.register(Policy)
admin.site.register(Treatment)
admin.site.register(ClaimSettlementinfo)
admin.site.register(Claim)
admin.site.register(Role)
# admin.site.register(Claim)
# admin.site.register(Benifits)