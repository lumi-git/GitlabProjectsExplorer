classDiagram
class observability_{group: observability_
description: group node}
class observability_ece-admin_{group: observability_ece-admin_
description: group node}
observability_ --> observability_ece-admin_
class observability_ece-admin_playbooks_{group: observability_ece-admin_playbooks_
description: group node}
observability_ece-admin_ --> observability_ece-admin_playbooks_
class observability_ece-admin_playbooks_services-socles-playbooks_{project: services-socles-playbooks
description: }
observability_ece-admin_playbooks_ --> observability_ece-admin_playbooks_services-socles-playbooks_
class observability_ece-admin_playbooks_ece-administration-playbooks_{project: ece-administration-playbooks
description: None}
observability_ece-admin_playbooks_ --> observability_ece-admin_playbooks_ece-administration-playbooks_
class observability_ece-admin_playbooks_services-socles-playbooks-tests_{project: services-socles-playbooks-tests
description: None}
observability_ece-admin_playbooks_ --> observability_ece-admin_playbooks_services-socles-playbooks-tests_
class observability_ece-admin_playbooks_tenant-observability-playbook_{project: tenant-observability-playbook
description: }
observability_ece-admin_playbooks_ --> observability_ece-admin_playbooks_tenant-observability-playbook_
class observability_ece-admin_debug_{group: observability_ece-admin_debug_
description: group node}
observability_ece-admin_ --> observability_ece-admin_debug_
class observability_ece-admin_debug_deploy-obs-example_{project: deploy-obs-example
description: None}
observability_ece-admin_debug_ --> observability_ece-admin_debug_deploy-obs-example_
class observability_ece-admin_inventories_{group: observability_ece-admin_inventories_
description: group node}
observability_ece-admin_ --> observability_ece-admin_inventories_
class observability_ece-admin_inventories_zone-cloudservices_{project: zone-cloudservices
description: }
observability_ece-admin_inventories_ --> observability_ece-admin_inventories_zone-cloudservices_
class observability_ece-admin_inventories_zone-management_{project: zone-management
description: }
observability_ece-admin_inventories_ --> observability_ece-admin_inventories_zone-management_
class observability_ece-admin_inventories_services_socles_zm_{project: services_socles_zm
description: }
observability_ece-admin_inventories_ --> observability_ece-admin_inventories_services_socles_zm_
class observability_ece-admin_inventories_services-socles-zcs_{project: services-socles-zcs
description: None}
observability_ece-admin_inventories_ --> observability_ece-admin_inventories_services-socles-zcs_
class observability_public_{group: observability_public_
description: group node}
observability_ --> observability_public_
class observability_public_roles_{group: observability_public_roles_
description: group node}
observability_public_ --> observability_public_roles_
class observability_public_roles_services-beats-tests_{project: services-beats-tests
description: Test de la bonne exécution des services filebeat, metricbeat et auditbeat}
observability_public_roles_ --> observability_public_roles_services-beats-tests_
class observability_public_roles_beats-install_{project: beats-install
description: None}
observability_public_roles_ --> observability_public_roles_beats-install_
class observability_public_roles_otelcol-install_{project: otelcol-install
description: None}
observability_public_roles_ --> observability_public_roles_otelcol-install_
class observability_public_roles_beats-delete_{project: beats-delete
description: None}
observability_public_roles_ --> observability_public_roles_beats-delete_
class observability_public_roles_heartbeat-delete_{project: heartbeat-delete
description: None}
observability_public_roles_ --> observability_public_roles_heartbeat-delete_
class observability_public_roles_heartbeat-install_{project: heartbeat-install
description: None}
observability_public_roles_ --> observability_public_roles_heartbeat-install_
class observability_public_roles_kibana-import-ressources_{project: kibana-import-ressources
description: None}
observability_public_roles_ --> observability_public_roles_kibana-import-ressources_
class observability_public_roles_heartbeat-add-monitor_{project: heartbeat-add-monitor
description: }
observability_public_roles_ --> observability_public_roles_heartbeat-add-monitor_
class observability_public_roles_logstash-delete_{project: logstash-delete
description: None}
observability_public_roles_ --> observability_public_roles_logstash-delete_
class observability_public_roles_logstash-install_{project: logstash-install
description: None}
observability_public_roles_ --> observability_public_roles_logstash-install_
class observability_public_roles_tenant-observability_{project: tenant-observability
description: None}
observability_public_roles_ --> observability_public_roles_tenant-observability_
class observability_public_roles_logstash-filebeat-delete_{project: logstash-filebeat-delete
description: None}
observability_public_roles_ --> observability_public_roles_logstash-filebeat-delete_
class observability_public_roles_logstash-filebeat-install_{project: logstash-filebeat-install
description: None}
observability_public_roles_ --> observability_public_roles_logstash-filebeat-install_
class observability_public_roles_beats-add-module_{project: beats-add-module
description: None}
observability_public_roles_ --> observability_public_roles_beats-add-module_
class observability_public_roles_logstash-configure_{project: logstash-configure
description: None}
observability_public_roles_ --> observability_public_roles_logstash-configure_
class observability_public_roles_otelcol-delete_{project: otelcol-delete
description: None}
observability_public_roles_ --> observability_public_roles_otelcol-delete_
class observability_public_roles_vault-get-secret_{project: vault-get-secret
description: None}
observability_public_roles_ --> observability_public_roles_vault-get-secret_
class ZM_C1NP_{group: ZM_C1NP_
description: group node}
class ZM_C1NP_ansible_{group: ZM_C1NP_ansible_
description: group node}
ZM_C1NP_ --> ZM_C1NP_ansible_
class ZM_C1NP_ansible_inventories_{group: ZM_C1NP_ansible_inventories_
description: group node}
ZM_C1NP_ansible_ --> ZM_C1NP_ansible_inventories_
class ZM_C1NP_ansible_inventories_zm_c1np_{group: ZM_C1NP_ansible_inventories_zm_c1np_
description: group node}
ZM_C1NP_ansible_inventories_ --> ZM_C1NP_ansible_inventories_zm_c1np_
class ZM_C1NP_ansible_inventories_zm_c1np_technical_{group: ZM_C1NP_ansible_inventories_zm_c1np_technical_
description: group node}
ZM_C1NP_ansible_inventories_zm_c1np_ --> ZM_C1NP_ansible_inventories_zm_c1np_technical_
class ZM_C1NP_ansible_inventories_zm_c1np_technical_gestion_zone_service_zee_{project: gestion_zone_service_zee
description: None}
ZM_C1NP_ansible_inventories_zm_c1np_technical_ --> ZM_C1NP_ansible_inventories_zm_c1np_technical_gestion_zone_service_zee_
class ZM_C1NP_ansible_inventories_zm_c1np_technical_gestion_exposition_tech_{project: gestion_exposition_tech
description: None}
ZM_C1NP_ansible_inventories_zm_c1np_technical_ --> ZM_C1NP_ansible_inventories_zm_c1np_technical_gestion_exposition_tech_
class ZM_C1NP_ansible_inventories_zm_c1np_technical_wsus_zm_tech_{project: wsus_zm_tech
description: None}
ZM_C1NP_ansible_inventories_zm_c1np_technical_ --> ZM_C1NP_ansible_inventories_zm_c1np_technical_wsus_zm_tech_
class ZM_C1NP_ansible_inventories_zm_c1np_technical_gestion_zones_{project: gestion_zones
description: None}
ZM_C1NP_ansible_inventories_zm_c1np_technical_ --> ZM_C1NP_ansible_inventories_zm_c1np_technical_gestion_zones_
class ZM_C1NP_ansible_inventories_zm_c1np_functional_{group: ZM_C1NP_ansible_inventories_zm_c1np_functional_
description: group node}
ZM_C1NP_ansible_inventories_zm_c1np_ --> ZM_C1NP_ansible_inventories_zm_c1np_functional_
class ZM_C1NP_ansible_inventories_zm_c1np_functional_wsus_zm_fct_{project: wsus_zm_fct
description: None}
ZM_C1NP_ansible_inventories_zm_c1np_functional_ --> ZM_C1NP_ansible_inventories_zm_c1np_functional_wsus_zm_fct_
class ZM_C1NP_ansible_inventories_zm_c1np_functional_gestion_zone_service_{project: gestion_zone_service
description: None}
ZM_C1NP_ansible_inventories_zm_c1np_functional_ --> ZM_C1NP_ansible_inventories_zm_c1np_functional_gestion_zone_service_
class ZM_C1NP_ansible_inventories_zm_c1np_functional_gestion_zone_projet_{project: gestion_zone_projet
description: None}
ZM_C1NP_ansible_inventories_zm_c1np_functional_ --> ZM_C1NP_ansible_inventories_zm_c1np_functional_gestion_zone_projet_
class ZM_C1NP_ansible_inventories_c1np_css_{group: ZM_C1NP_ansible_inventories_c1np_css_
description: group node}
ZM_C1NP_ansible_inventories_ --> ZM_C1NP_ansible_inventories_c1np_css_
class ZM_C1NP_ansible_inventories_c1np_css_technical_{group: ZM_C1NP_ansible_inventories_c1np_css_technical_
description: group node}
ZM_C1NP_ansible_inventories_c1np_css_ --> ZM_C1NP_ansible_inventories_c1np_css_technical_
class ZM_C1NP_ansible_inventories_c1np_css_technical_wsus_css_tech_{project: wsus_css_tech
description: None}
ZM_C1NP_ansible_inventories_c1np_css_technical_ --> ZM_C1NP_ansible_inventories_c1np_css_technical_wsus_css_tech_
class ZM_C1NP_ansible_inventories_c1np_css_technical_rhsso_css_tech_{project: rhsso_css_tech
description: None}
ZM_C1NP_ansible_inventories_c1np_css_technical_ --> ZM_C1NP_ansible_inventories_c1np_css_technical_rhsso_css_tech_
class ZM_C1NP_ansible_inventories_c1np_css_technical_gitlab_css_tech_{project: gitlab_css_tech
description: None}
ZM_C1NP_ansible_inventories_c1np_css_technical_ --> ZM_C1NP_ansible_inventories_c1np_css_technical_gitlab_css_tech_
class ZM_C1NP_ansible_inventories_c1np_css_technical_commandements_css_tech_{project: commandements_css_tech
description: None}
ZM_C1NP_ansible_inventories_c1np_css_technical_ --> ZM_C1NP_ansible_inventories_c1np_css_technical_commandements_css_tech_
class ZM_C1NP_ansible_inventories_c1np_css_technical_artifactory_css_tech_{project: artifactory_css_tech
description: None}
ZM_C1NP_ansible_inventories_c1np_css_technical_ --> ZM_C1NP_ansible_inventories_c1np_css_technical_artifactory_css_tech_
class ZM_C1NP_ansible_inventories_c1np_css_technical_aap_css_tech_{project: aap_css_tech
description: None}
ZM_C1NP_ansible_inventories_c1np_css_technical_ --> ZM_C1NP_ansible_inventories_c1np_css_technical_aap_css_tech_
class ZM_C1NP_ansible_inventories_c1np_css_functional_{group: ZM_C1NP_ansible_inventories_c1np_css_functional_
description: group node}
ZM_C1NP_ansible_inventories_c1np_css_ --> ZM_C1NP_ansible_inventories_c1np_css_functional_
class ZM_C1NP_ansible_inventories_c1np_css_functional_wsus_css_fct_{project: wsus_css_fct
description: None}
ZM_C1NP_ansible_inventories_c1np_css_functional_ --> ZM_C1NP_ansible_inventories_c1np_css_functional_wsus_css_fct_
class ZM_C1NP_ansible_inventories_c1np_css_functional_rhsso_css_fct_{project: rhsso_css_fct
description: None}
ZM_C1NP_ansible_inventories_c1np_css_functional_ --> ZM_C1NP_ansible_inventories_c1np_css_functional_rhsso_css_fct_
class ZM_C1NP_ansible_inventories_c1np_css_functional_gitlab_css_fct_{project: gitlab_css_fct
description: None}
ZM_C1NP_ansible_inventories_c1np_css_functional_ --> ZM_C1NP_ansible_inventories_c1np_css_functional_gitlab_css_fct_
class ZM_C1NP_ansible_inventories_c1np_css_functional_commandements_css_fct_{project: commandements_css_fct
description: None}
ZM_C1NP_ansible_inventories_c1np_css_functional_ --> ZM_C1NP_ansible_inventories_c1np_css_functional_commandements_css_fct_
class ZM_C1NP_ansible_inventories_c1np_css_functional_artifactory_css_fct_{project: artifactory_css_fct
description: None}
ZM_C1NP_ansible_inventories_c1np_css_functional_ --> ZM_C1NP_ansible_inventories_c1np_css_functional_artifactory_css_fct_
class ZM_C1NP_ansible_inventories_c1np_css_functional_aap_css_fct_{project: aap_css_fct
description: None}
ZM_C1NP_ansible_inventories_c1np_css_functional_ --> ZM_C1NP_ansible_inventories_c1np_css_functional_aap_css_fct_
class ZM_C1NP_ansible_playbooks_{group: ZM_C1NP_ansible_playbooks_
description: group node}
ZM_C1NP_ansible_ --> ZM_C1NP_ansible_playbooks_
class ZM_C1NP_ansible_playbooks_Gestion_exposition_drive_{project: Gestion_exposition_drive
description: None}
ZM_C1NP_ansible_playbooks_ --> ZM_C1NP_ansible_playbooks_Gestion_exposition_drive_
class ZM_C1NP_ansible_playbooks_deploy_wsus_{project: deploy_wsus
description: None}
ZM_C1NP_ansible_playbooks_ --> ZM_C1NP_ansible_playbooks_deploy_wsus_
class ZM_C1NP_ansible_playbooks_remediation_{project: remediation
description: None}
ZM_C1NP_ansible_playbooks_ --> ZM_C1NP_ansible_playbooks_remediation_
class ZM_C1NP_ansible_playbooks_desenrolement_{project: desenrolement
description: None}
ZM_C1NP_ansible_playbooks_ --> ZM_C1NP_ansible_playbooks_desenrolement_
class ZM_C1NP_ansible_playbooks_gestion_zone_tenant_{project: gestion_zone_tenant
description: None}
ZM_C1NP_ansible_playbooks_ --> ZM_C1NP_ansible_playbooks_gestion_zone_tenant_
class ZM_C1NP_ansible_playbooks_gestion_zone_test_auto_{project: gestion_zone_test_auto
description: None}
ZM_C1NP_ansible_playbooks_ --> ZM_C1NP_ansible_playbooks_gestion_zone_test_auto_
class ZM_C1NP_ansible_playbooks_gestion_zone_infra_{project: gestion_zone_infra
description: None}
ZM_C1NP_ansible_playbooks_ --> ZM_C1NP_ansible_playbooks_gestion_zone_infra_
class ZM_C1NP_ansible_roles_{group: ZM_C1NP_ansible_roles_
description: group node}
ZM_C1NP_ansible_ --> ZM_C1NP_ansible_roles_
class ZM_C1NP_ansible_roles_commandements_{group: ZM_C1NP_ansible_roles_commandements_
description: group node}
ZM_C1NP_ansible_roles_ --> ZM_C1NP_ansible_roles_commandements_
class ZM_C1NP_ansible_roles_commandements_service-aap_{project: service-aap
description: None}
ZM_C1NP_ansible_roles_commandements_ --> ZM_C1NP_ansible_roles_commandements_service-aap_
class ZM_C1NP_ansible_roles_role-terraform-drive_{project: role-terraform-drive
description: Rôle de pilotage de terraform}
ZM_C1NP_ansible_roles_ --> ZM_C1NP_ansible_roles_role-terraform-drive_
class ZM_C1NP_ansible_roles_role-ldaps-drive-ad_{project: role-ldaps-drive-ad
description: Rôle de création des objets de l'AD en utilisant ansible pour piloter LDAPS}
ZM_C1NP_ansible_roles_ --> ZM_C1NP_ansible_roles_role-ldaps-drive-ad_
class ZM_C1NP_cloudmaker_{group: ZM_C1NP_cloudmaker_
description: group node}
ZM_C1NP_ --> ZM_C1NP_cloudmaker_
class ZM_C1NP_cloudmaker_gestion_exposition_{group: ZM_C1NP_cloudmaker_gestion_exposition_
description: group node}
ZM_C1NP_cloudmaker_ --> ZM_C1NP_cloudmaker_gestion_exposition_
class ZM_C1NP_cloudmaker_gestion_exposition_Gestion_exposition-runtime_{project: Gestion_exposition-runtime
description: None}
ZM_C1NP_cloudmaker_gestion_exposition_ --> ZM_C1NP_cloudmaker_gestion_exposition_Gestion_exposition-runtime_
class ZM_C1NP_delivery_{group: ZM_C1NP_delivery_
description: group node}
ZM_C1NP_ --> ZM_C1NP_delivery_
class ZM_C1NP_delivery_gestion_exposition_{project: gestion_exposition
description: None}
ZM_C1NP_delivery_ --> ZM_C1NP_delivery_gestion_exposition_
class ZM_C1NP_delivery_service-livraison_{project: service-livraison
description: None}
ZM_C1NP_delivery_ --> ZM_C1NP_delivery_service-livraison_
class ZM_C1NP_delivery_commandements_{project: commandements
description: None}
ZM_C1NP_delivery_ --> ZM_C1NP_delivery_commandements_
class ZM_C1NP_delivery_gestion_zone_{project: gestion_zone
description: None}
ZM_C1NP_delivery_ --> ZM_C1NP_delivery_gestion_zone_
class ZM_C1NP_ruche_{group: ZM_C1NP_ruche_
description: group node}
ZM_C1NP_ --> ZM_C1NP_ruche_
class ZM_C1NP_ruche_synchronisationah_{project: synchronisationah
description: }
ZM_C1NP_ruche_ --> ZM_C1NP_ruche_synchronisationah_
class ZM_C1NP_service-de-livraison-import_{project: Service de livraison import
description: None}
ZM_C1NP_ --> ZM_C1NP_service-de-livraison-import_
class ZM_C1NP_tests_bout_en_bout_{project: tests_bout_en_bout
description: None}
ZM_C1NP_ --> ZM_C1NP_tests_bout_en_bout_
class ZM_C1NP_vra_{group: ZM_C1NP_vra_
description: group node}
ZM_C1NP_ --> ZM_C1NP_vra_
class ZM_C1NP_vra_workflows_{project: workflows
description: None}
ZM_C1NP_vra_ --> ZM_C1NP_vra_workflows_
class ZM_C1NP_vra_custom_form_{project: custom_form
description: None}
ZM_C1NP_vra_ --> ZM_C1NP_vra_custom_form_
class ZM_C1NP_vra_blueprints_{project: blueprints
description: }
ZM_C1NP_vra_ --> ZM_C1NP_vra_blueprints_
class ZP_C1NP_{group: ZP_C1NP_
description: group node}
class ZP_C1NP_ansible_{group: ZP_C1NP_ansible_
description: group node}
ZP_C1NP_ --> ZP_C1NP_ansible_
class ZP_C1NP_ansible_playbooks_{group: ZP_C1NP_ansible_playbooks_
description: group node}
ZP_C1NP_ansible_ --> ZP_C1NP_ansible_playbooks_
class ZP_C1NP_ansible_playbooks_deploy_wsus_{project: deploy_wsus
description: None}
ZP_C1NP_ansible_playbooks_ --> ZP_C1NP_ansible_playbooks_deploy_wsus_
class SVC_CDP_GITCSC_W_{group: SVC_CDP_GITCSC_W_
description: group node}
class SVC_CDP_GITCSC_W_blueprint_{project: Blueprint
description: }
SVC_CDP_GITCSC_W_ --> SVC_CDP_GITCSC_W_blueprint_
class ZP_DevSecOps_{group: ZP_DevSecOps_
description: group node}
class ZP_DevSecOps_roles_{group: ZP_DevSecOps_roles_
description: group node}
ZP_DevSecOps_ --> ZP_DevSecOps_roles_
class ZP_DevSecOps_roles_ansible-automation-platform_{group: ZP_DevSecOps_roles_ansible-automation-platform_
description: group node}
ZP_DevSecOps_roles_ --> ZP_DevSecOps_roles_ansible-automation-platform_
class ZP_DevSecOps_roles_ansible-automation-platform_ee-manager_{project: ee-manager
description: None}
ZP_DevSecOps_roles_ansible-automation-platform_ --> ZP_DevSecOps_roles_ansible-automation-platform_ee-manager_
class ZP_DevSecOps_roles_ansible-automation-platform_rbac_{project: rbac
description: None}
ZP_DevSecOps_roles_ansible-automation-platform_ --> ZP_DevSecOps_roles_ansible-automation-platform_rbac_
class ZP_DevSecOps_roles_ansible-automation-platform_authentication_{project: authentication
description: None}
ZP_DevSecOps_roles_ansible-automation-platform_ --> ZP_DevSecOps_roles_ansible-automation-platform_authentication_
class ZP_DevSecOps_roles_ansible-automation-platform_install_{project: install
description: None}
ZP_DevSecOps_roles_ansible-automation-platform_ --> ZP_DevSecOps_roles_ansible-automation-platform_install_
class ZP_DevSecOps_roles_ansible-automation-platform_inventory_{project: inventory
description: None}
ZP_DevSecOps_roles_ansible-automation-platform_ --> ZP_DevSecOps_roles_ansible-automation-platform_inventory_
class ZP_DevSecOps_roles_docker-role_{project: docker-role
description: None}
ZP_DevSecOps_roles_ --> ZP_DevSecOps_roles_docker-role_
class ZP_DevSecOps_playbooks_{group: ZP_DevSecOps_playbooks_
description: group node}
ZP_DevSecOps_ --> ZP_DevSecOps_playbooks_
class ZP_DevSecOps_playbooks_aap2-playbook_{project: aap2-playbook
description: None}
ZP_DevSecOps_playbooks_ --> ZP_DevSecOps_playbooks_aap2-playbook_
class ZP_DevSecOps_forks_{group: ZP_DevSecOps_forks_
description: group node}
ZP_DevSecOps_ --> ZP_DevSecOps_forks_
class ZP_DevSecOps_forks_jenkins-role_{project: jenkins-role
description: None}
ZP_DevSecOps_forks_ --> ZP_DevSecOps_forks_jenkins-role_
class ZP_DevSecOps_forks_jenkins-playbook_{project: jenkins-playbook
description: None}
ZP_DevSecOps_forks_ --> ZP_DevSecOps_forks_jenkins-playbook_
class zp_cortex1gds_{group: zp_cortex1gds_
description: group node}
class zp_cortex1gds_roles_{group: zp_cortex1gds_roles_
description: group node}
zp_cortex1gds_ --> zp_cortex1gds_roles_
class zp_cortex1gds_roles_vault-get-cert_{project: vault-get-cert
description: None}
zp_cortex1gds_roles_ --> zp_cortex1gds_roles_vault-get-cert_
class zp_cortex1gds_roles_vault-agent_{project: vault-agent
description: None}
zp_cortex1gds_roles_ --> zp_cortex1gds_roles_vault-agent_
class zp_cortex1gds_roles_vault-approle_{project: vault-approle
description: None}
zp_cortex1gds_roles_ --> zp_cortex1gds_roles_vault-approle_
class zp_cores_{group: zp_cores_
description: group node}
class zp_cores_roles_{group: zp_cores_roles_
description: group node}
zp_cores_ --> zp_cores_roles_
class zp_cores_roles_rhsso-realm_{project: rhsso-realm
description: None}
zp_cores_roles_ --> zp_cores_roles_rhsso-realm_
class zp_cores_roles_rhsso-hardening_{project: rhsso-hardening
description: None}
zp_cores_roles_ --> zp_cores_roles_rhsso-hardening_
class zp_cores_roles_rhsso-patch_{project: rhsso-patch
description: None}
zp_cores_roles_ --> zp_cores_roles_rhsso-patch_
class zp_cores_roles_rhsso-database_{project: rhsso-database
description: None}
zp_cores_roles_ --> zp_cores_roles_rhsso-database_
class zp_cores_roles_rhsso_{project: rhsso
description: None}
zp_cores_roles_ --> zp_cores_roles_rhsso_
class zp_cores_roles_create-user_{project: create-user
description: None}
zp_cores_roles_ --> zp_cores_roles_create-user_
class zp_cores_playbooks_{group: zp_cores_playbooks_
description: group node}
zp_cores_ --> zp_cores_playbooks_
class zp_cores_playbooks_deploy-rhsso_{project: deploy-rhsso
description: None}
zp_cores_playbooks_ --> zp_cores_playbooks_deploy-rhsso_
class snum-common_{group: snum-common_
description: group node}
class snum-common_roles_{group: snum-common_roles_
description: group node}
snum-common_ --> snum-common_roles_
class snum-common_roles_haproxy_{project: haproxy
description: None}
snum-common_roles_ --> snum-common_roles_haproxy_
class snum-common_roles_mariadb_{project: mariadb
description: None}
snum-common_roles_ --> snum-common_roles_mariadb_
class snum-common_roles_nginx_dso_{project: nginx_dso
description: None}
snum-common_roles_ --> snum-common_roles_nginx_dso_
class ansible_{group: ansible_
description: group node}
class ansible_roles_{group: ansible_roles_
description: group node}
ansible_ --> ansible_roles_
class ansible_roles_system_{group: ansible_roles_system_
description: group node}
ansible_roles_ --> ansible_roles_system_
class ansible_roles_system_rsyslog_{project: rsyslog
description: None}
ansible_roles_system_ --> ansible_roles_system_rsyslog_
class ansible_roles_system_logrotate_{project: logrotate
description: None}
ansible_roles_system_ --> ansible_roles_system_logrotate_
class ansible_roles_utils_{group: ansible_roles_utils_
description: group node}
ansible_roles_ --> ansible_roles_utils_
class ansible_roles_utils_check_{project: check
description: None}
ansible_roles_utils_ --> ansible_roles_utils_check_
class ZP_MEDUSA_{group: ZP_MEDUSA_
description: group node}
class ZP_MEDUSA_roles_{group: ZP_MEDUSA_roles_
description: group node}
ZP_MEDUSA_ --> ZP_MEDUSA_roles_
class ZP_MEDUSA_roles_medusa-api_{project: medusa-api
description: None}
ZP_MEDUSA_roles_ --> ZP_MEDUSA_roles_medusa-api_
class ZP_MEDUSA_roles_medusa-client_{project: medusa-client
description: None}
ZP_MEDUSA_roles_ --> ZP_MEDUSA_roles_medusa-client_
class ZP_MEDUSA_roles_fsecure-import_{project: fsecure-import
description: None}
ZP_MEDUSA_roles_ --> ZP_MEDUSA_roles_fsecure-import_
class ZP_MEDUSA_roles_download-av_{project: download-av
description: None}
ZP_MEDUSA_roles_ --> ZP_MEDUSA_roles_download-av_
class ZP_MEDUSA_roles_package-av_{project: package-av
description: None}
ZP_MEDUSA_roles_ --> ZP_MEDUSA_roles_package-av_
class ZP_MEDUSA_roles_apache-windows_{project: apache-windows
description: None}
ZP_MEDUSA_roles_ --> ZP_MEDUSA_roles_apache-windows_
class ZP_MEDUSA_roles_wsus_{project: wsus
description: None}
ZP_MEDUSA_roles_ --> ZP_MEDUSA_roles_wsus_
