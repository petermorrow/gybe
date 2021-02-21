# generated by datamodel-codegen:
#   filename:  _definitions.json
#   timestamp: 2021-01-20T05:35:16+00:00

from __future__ import annotations

from enum import Enum
from typing import Any, List

import pydantic as pyd


class Model(pyd.BaseModel):
    __root__: Any


class Kind(Enum):
    MutatingWebhookConfiguration = 'MutatingWebhookConfiguration'


class Kind1(Enum):
    MutatingWebhookConfigurationList = 'MutatingWebhookConfigurationList'


class Kind2(Enum):
    ValidatingWebhookConfiguration = 'ValidatingWebhookConfiguration'


class Kind3(Enum):
    ValidatingWebhookConfigurationList = 'ValidatingWebhookConfigurationList'


class Kind4(Enum):
    MutatingWebhookConfiguration = 'MutatingWebhookConfiguration'


class Kind5(Enum):
    MutatingWebhookConfigurationList = 'MutatingWebhookConfigurationList'


class Kind6(Enum):
    ValidatingWebhookConfiguration = 'ValidatingWebhookConfiguration'


class Kind7(Enum):
    ValidatingWebhookConfigurationList = 'ValidatingWebhookConfigurationList'


class Kind8(Enum):
    StorageVersion = 'StorageVersion'


class Kind9(Enum):
    StorageVersionList = 'StorageVersionList'


class Kind10(Enum):
    ControllerRevision = 'ControllerRevision'


class Kind11(Enum):
    ControllerRevisionList = 'ControllerRevisionList'


class Kind12(Enum):
    DaemonSet = 'DaemonSet'


class Kind13(Enum):
    DaemonSetList = 'DaemonSetList'


class Kind14(Enum):
    Deployment = 'Deployment'


class Kind15(Enum):
    DeploymentList = 'DeploymentList'


class Kind16(Enum):
    ReplicaSet = 'ReplicaSet'


class Kind17(Enum):
    ReplicaSetList = 'ReplicaSetList'


class Kind18(Enum):
    StatefulSet = 'StatefulSet'


class Kind19(Enum):
    StatefulSetList = 'StatefulSetList'


class Kind20(Enum):
    TokenRequest = 'TokenRequest'


class Kind21(Enum):
    TokenReview = 'TokenReview'


class Extra(pyd.BaseModel):
    __root__: List[str]


class Kind22(Enum):
    TokenReview = 'TokenReview'


class Kind23(Enum):
    LocalSubjectAccessReview = 'LocalSubjectAccessReview'


class Kind24(Enum):
    SelfSubjectAccessReview = 'SelfSubjectAccessReview'


class Kind25(Enum):
    SelfSubjectRulesReview = 'SelfSubjectRulesReview'


class Kind26(Enum):
    SubjectAccessReview = 'SubjectAccessReview'


class Kind27(Enum):
    LocalSubjectAccessReview = 'LocalSubjectAccessReview'


class Kind28(Enum):
    SelfSubjectAccessReview = 'SelfSubjectAccessReview'


class Kind29(Enum):
    SelfSubjectRulesReview = 'SelfSubjectRulesReview'


class Kind30(Enum):
    SubjectAccessReview = 'SubjectAccessReview'


class Kind31(Enum):
    HorizontalPodAutoscaler = 'HorizontalPodAutoscaler'


class Kind32(Enum):
    HorizontalPodAutoscalerList = 'HorizontalPodAutoscalerList'


class Kind33(Enum):
    Scale = 'Scale'


class Kind34(Enum):
    HorizontalPodAutoscaler = 'HorizontalPodAutoscaler'


class Kind35(Enum):
    HorizontalPodAutoscalerList = 'HorizontalPodAutoscalerList'


class Kind36(Enum):
    HorizontalPodAutoscaler = 'HorizontalPodAutoscaler'


class Kind37(Enum):
    HorizontalPodAutoscalerList = 'HorizontalPodAutoscalerList'


class Kind38(Enum):
    Job = 'Job'


class Kind39(Enum):
    JobList = 'JobList'


class Kind40(Enum):
    CronJob = 'CronJob'


class Kind41(Enum):
    CronJobList = 'CronJobList'


class Kind42(Enum):
    CronJob = 'CronJob'


class Kind43(Enum):
    CronJobList = 'CronJobList'


class Kind44(Enum):
    CertificateSigningRequest = 'CertificateSigningRequest'


class Kind45(Enum):
    CertificateSigningRequestList = 'CertificateSigningRequestList'


class Kind46(Enum):
    CertificateSigningRequest = 'CertificateSigningRequest'


class Kind47(Enum):
    CertificateSigningRequestList = 'CertificateSigningRequestList'


class Kind48(Enum):
    Lease = 'Lease'


class Kind49(Enum):
    LeaseList = 'LeaseList'


class Kind50(Enum):
    Lease = 'Lease'


class Kind51(Enum):
    LeaseList = 'LeaseList'


class Kind52(Enum):
    Binding = 'Binding'


class VolumeAttributes(pyd.BaseModel):
    pass

    class Config:
        extra = pyd.Extra.allow


class Kind53(Enum):
    ComponentStatus = 'ComponentStatus'


class Kind54(Enum):
    ComponentStatusList = 'ComponentStatusList'


BinaryData = bytes
Data = str


class Kind55(Enum):
    ConfigMap = 'ConfigMap'


class Kind56(Enum):
    ConfigMapList = 'ConfigMapList'


class Kind57(Enum):
    Endpoints = 'Endpoints'


class Kind58(Enum):
    EndpointsList = 'EndpointsList'


class Kind59(Enum):
    EphemeralContainers = 'EphemeralContainers'


class Kind60(Enum):
    Event = 'Event'


class Kind61(Enum):
    EventList = 'EventList'


class Options(pyd.BaseModel):
    pass

    class Config:
        extra = pyd.Extra.allow


class Kind62(Enum):
    LimitRange = 'LimitRange'


class Default(pyd.BaseModel):
    pass


class DefaultRequest(pyd.BaseModel):
    pass


class Max(pyd.BaseModel):
    pass


class MaxLimitRequestRatio(pyd.BaseModel):
    pass


class Min(pyd.BaseModel):
    pass


class Kind63(Enum):
    LimitRangeList = 'LimitRangeList'


class Kind64(Enum):
    Namespace = 'Namespace'


class Kind65(Enum):
    NamespaceList = 'NamespaceList'


class Kind66(Enum):
    Node = 'Node'


class Kind67(Enum):
    NodeList = 'NodeList'


class Allocatable(pyd.BaseModel):
    pass


Capacity = str


class Kind68(Enum):
    PersistentVolume = 'PersistentVolume'


class Kind69(Enum):
    PersistentVolumeClaim = 'PersistentVolumeClaim'


class Kind70(Enum):
    PersistentVolumeClaimList = 'PersistentVolumeClaimList'


class Kind71(Enum):
    PersistentVolumeList = 'PersistentVolumeList'


class Kind72(Enum):
    Pod = 'Pod'


class Kind73(Enum):
    PodList = 'PodList'


class NodeSelector(pyd.BaseModel):
    pass

    class Config:
        extra = pyd.Extra.allow


class Overhead(pyd.BaseModel):
    pass


class Kind74(Enum):
    PodTemplate = 'PodTemplate'


class Kind75(Enum):
    PodTemplateList = 'PodTemplateList'


class Kind76(Enum):
    ReplicationController = 'ReplicationController'


class Kind77(Enum):
    ReplicationControllerList = 'ReplicationControllerList'


Selector = str


class Kind78(Enum):
    ResourceQuota = 'ResourceQuota'


class Kind79(Enum):
    ResourceQuotaList = 'ResourceQuotaList'


Hard = str
Used = str
Limits = str
Requests = str


class Kind80(Enum):
    Secret = 'Secret'


class StringData(pyd.BaseModel):
    pass

    class Config:
        extra = pyd.Extra.allow


class Kind81(Enum):
    SecretList = 'SecretList'


class Kind82(Enum):
    Service = 'Service'


class Kind83(Enum):
    ServiceAccount = 'ServiceAccount'


class Kind84(Enum):
    ServiceAccountList = 'ServiceAccountList'


class Kind85(Enum):
    ServiceList = 'ServiceList'


class Topology(pyd.BaseModel):
    pass

    class Config:
        extra = pyd.Extra.allow


class Kind86(Enum):
    EndpointSlice = 'EndpointSlice'


class Kind87(Enum):
    EndpointSliceList = 'EndpointSliceList'


class Kind88(Enum):
    Event = 'Event'


class Kind89(Enum):
    EventList = 'EventList'


class Kind90(Enum):
    Event = 'Event'


class Kind91(Enum):
    EventList = 'EventList'


class Kind92(Enum):
    Ingress = 'Ingress'


class Kind93(Enum):
    IngressList = 'IngressList'


class Kind94(Enum):
    FlowSchema = 'FlowSchema'


class Kind95(Enum):
    FlowSchemaList = 'FlowSchemaList'


class Kind96(Enum):
    PriorityLevelConfiguration = 'PriorityLevelConfiguration'


class Kind97(Enum):
    PriorityLevelConfigurationList = 'PriorityLevelConfigurationList'


class Kind98(Enum):
    FlowSchema = 'FlowSchema'


class Kind99(Enum):
    FlowSchemaList = 'FlowSchemaList'


class Kind100(Enum):
    PriorityLevelConfiguration = 'PriorityLevelConfiguration'


class Kind101(Enum):
    PriorityLevelConfigurationList = 'PriorityLevelConfigurationList'


class Kind102(Enum):
    Ingress = 'Ingress'


class Kind103(Enum):
    IngressClass = 'IngressClass'


class Kind104(Enum):
    IngressClassList = 'IngressClassList'


class Kind105(Enum):
    IngressList = 'IngressList'


class Kind106(Enum):
    NetworkPolicy = 'NetworkPolicy'


class Kind107(Enum):
    NetworkPolicyList = 'NetworkPolicyList'


class Kind108(Enum):
    Ingress = 'Ingress'


class Kind109(Enum):
    IngressClass = 'IngressClass'


class Kind110(Enum):
    IngressClassList = 'IngressClassList'


class Kind111(Enum):
    IngressList = 'IngressList'


class PodFixed(pyd.BaseModel):
    pass


class Kind112(Enum):
    RuntimeClass = 'RuntimeClass'


class Kind113(Enum):
    RuntimeClassList = 'RuntimeClassList'


class Kind114(Enum):
    RuntimeClass = 'RuntimeClass'


class Kind115(Enum):
    RuntimeClassList = 'RuntimeClassList'


class Kind116(Enum):
    RuntimeClass = 'RuntimeClass'


class Kind117(Enum):
    RuntimeClassList = 'RuntimeClassList'


class Kind118(Enum):
    Eviction = 'Eviction'


class Kind119(Enum):
    PodDisruptionBudget = 'PodDisruptionBudget'


class Kind120(Enum):
    PodDisruptionBudgetList = 'PodDisruptionBudgetList'


class DisruptedPods(pyd.BaseModel):
    pass


class Kind121(Enum):
    PodSecurityPolicy = 'PodSecurityPolicy'


class Kind122(Enum):
    PodSecurityPolicyList = 'PodSecurityPolicyList'


class Kind123(Enum):
    ClusterRole = 'ClusterRole'


class Kind124(Enum):
    ClusterRoleBinding = 'ClusterRoleBinding'


class Kind125(Enum):
    ClusterRoleBindingList = 'ClusterRoleBindingList'


class Kind126(Enum):
    ClusterRoleList = 'ClusterRoleList'


class Kind127(Enum):
    Role = 'Role'


class Kind128(Enum):
    RoleBinding = 'RoleBinding'


class Kind129(Enum):
    RoleBindingList = 'RoleBindingList'


class Kind130(Enum):
    RoleList = 'RoleList'


class Kind131(Enum):
    ClusterRole = 'ClusterRole'


class Kind132(Enum):
    ClusterRoleBinding = 'ClusterRoleBinding'


class Kind133(Enum):
    ClusterRoleBindingList = 'ClusterRoleBindingList'


class Kind134(Enum):
    ClusterRoleList = 'ClusterRoleList'


class Kind135(Enum):
    Role = 'Role'


class Kind136(Enum):
    RoleBinding = 'RoleBinding'


class Kind137(Enum):
    RoleBindingList = 'RoleBindingList'


class Kind138(Enum):
    RoleList = 'RoleList'


class Kind139(Enum):
    ClusterRole = 'ClusterRole'


class Kind140(Enum):
    ClusterRoleBinding = 'ClusterRoleBinding'


class Kind141(Enum):
    ClusterRoleBindingList = 'ClusterRoleBindingList'


class Kind142(Enum):
    ClusterRoleList = 'ClusterRoleList'


class Kind143(Enum):
    Role = 'Role'


class Kind144(Enum):
    RoleBinding = 'RoleBinding'


class Kind145(Enum):
    RoleBindingList = 'RoleBindingList'


class Kind146(Enum):
    RoleList = 'RoleList'


class Kind147(Enum):
    PriorityClass = 'PriorityClass'


class Kind148(Enum):
    PriorityClassList = 'PriorityClassList'


class Kind149(Enum):
    PriorityClass = 'PriorityClass'


class Kind150(Enum):
    PriorityClassList = 'PriorityClassList'


class Kind151(Enum):
    PriorityClass = 'PriorityClass'


class Kind152(Enum):
    PriorityClassList = 'PriorityClassList'


class Kind153(Enum):
    CSIDriver = 'CSIDriver'


class Kind154(Enum):
    CSIDriverList = 'CSIDriverList'


class Kind155(Enum):
    CSINode = 'CSINode'


class Kind156(Enum):
    CSINodeList = 'CSINodeList'


class Kind157(Enum):
    StorageClass = 'StorageClass'


class Parameters(pyd.BaseModel):
    pass

    class Config:
        extra = pyd.Extra.allow


class Kind158(Enum):
    StorageClassList = 'StorageClassList'


class Kind159(Enum):
    VolumeAttachment = 'VolumeAttachment'


class Kind160(Enum):
    VolumeAttachmentList = 'VolumeAttachmentList'


class AttachmentMetadata(pyd.BaseModel):
    pass

    class Config:
        extra = pyd.Extra.allow


class Kind161(Enum):
    CSIStorageCapacity = 'CSIStorageCapacity'


class Kind162(Enum):
    CSIStorageCapacityList = 'CSIStorageCapacityList'


class Kind163(Enum):
    VolumeAttachment = 'VolumeAttachment'


class Kind164(Enum):
    VolumeAttachmentList = 'VolumeAttachmentList'


class Kind165(Enum):
    CSIDriver = 'CSIDriver'


class Kind166(Enum):
    CSIDriverList = 'CSIDriverList'


class Kind167(Enum):
    CSINode = 'CSINode'


class Kind168(Enum):
    CSINodeList = 'CSINodeList'


class Kind169(Enum):
    StorageClass = 'StorageClass'


class Kind170(Enum):
    StorageClassList = 'StorageClassList'


class Kind171(Enum):
    VolumeAttachment = 'VolumeAttachment'


class Kind172(Enum):
    VolumeAttachmentList = 'VolumeAttachmentList'


class Kind173(Enum):
    CustomResourceDefinition = 'CustomResourceDefinition'


class Kind174(Enum):
    CustomResourceDefinitionList = 'CustomResourceDefinitionList'


class Definitions(pyd.BaseModel):
    pass


class Dependencies(pyd.BaseModel):
    pass


class PatternProperties(pyd.BaseModel):
    pass


class Properties(pyd.BaseModel):
    pass


class Kind175(Enum):
    CustomResourceDefinition = 'CustomResourceDefinition'


class Kind176(Enum):
    CustomResourceDefinitionList = 'CustomResourceDefinitionList'


class Kind177(Enum):
    APIGroup = 'APIGroup'


class Kind178(Enum):
    APIGroupList = 'APIGroupList'


class Kind179(Enum):
    APIResourceList = 'APIResourceList'


class Kind180(Enum):
    APIVersions = 'APIVersions'


class Kind181(Enum):
    DeleteOptions = 'DeleteOptions'


MatchLabels = str
Annotations = str
Labels = str


class Kind182(Enum):
    Status = 'Status'


class Kind183(Enum):
    APIService = 'APIService'


class Kind184(Enum):
    APIServiceList = 'APIServiceList'


class Kind185(Enum):
    APIService = 'APIService'


class Kind186(Enum):
    APIServiceList = 'APIServiceList'
