# generated by datamodel-codegen:
#   filename:  _definitions.json
#   timestamp: 2021-01-20T05:35:16+00:00

from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Field

from ..... import Kind123, Kind124, Kind125, Kind126, Kind127, Kind128, Kind129, Kind130
from ...apimachinery.pkg.apis.meta import v1


class PolicyRule(BaseModel):
    apiGroups: Optional[List[str]] = Field(
        None,
        description='APIGroups is the name of the APIGroup that contains the resources.  If multiple API groups are specified, any action requested against one of the enumerated resources in any API group will be allowed.',
    )
    nonResourceURLs: Optional[List[str]] = Field(
        None,
        description='NonResourceURLs is a set of partial urls that a user should have access to.  *s are allowed, but only as the full, final step in the path Since non-resource URLs are not namespaced, this field is only applicable for ClusterRoles referenced from a ClusterRoleBinding. Rules can either apply to API resources (such as "pods" or "secrets") or non-resource URL paths (such as "/api"),  but not both.',
    )
    resourceNames: Optional[List[str]] = Field(
        None,
        description='ResourceNames is an optional white list of names that the rule applies to.  An empty set means that everything is allowed.',
    )
    resources: Optional[List[str]] = Field(
        None,
        description='Resources is a list of resources this rule applies to.  ResourceAll represents all resources.',
    )
    verbs: List[str] = Field(
        ...,
        description='Verbs is a list of Verbs that apply to ALL the ResourceKinds and AttributeRestrictions contained in this rule.  VerbAll represents all kinds.',
    )


class RoleRef(BaseModel):
    apiGroup: str = Field(
        ..., description='APIGroup is the group for the resource being referenced'
    )
    kind: str = Field(..., description='Kind is the type of resource being referenced')
    name: str = Field(..., description='Name is the name of resource being referenced')


class Subject(BaseModel):
    apiGroup: Optional[str] = Field(
        None,
        description='APIGroup holds the API group of the referenced subject. Defaults to "" for ServiceAccount subjects. Defaults to "rbac.authorization.k8s.io" for User and Group subjects.',
    )
    kind: str = Field(
        ...,
        description='Kind of object being referenced. Values defined by this API group are "User", "Group", and "ServiceAccount". If the Authorizer does not recognized the kind value, the Authorizer should report an error.',
    )
    name: str = Field(..., description='Name of the object being referenced.')
    namespace: Optional[str] = Field(
        None,
        description='Namespace of the referenced object.  If the object kind is non-namespace, such as "User" or "Group", and this value is not empty the Authorizer should report an error.',
    )


class AggregationRule(BaseModel):
    clusterRoleSelectors: Optional[List[v1.LabelSelector]] = Field(
        None,
        description="ClusterRoleSelectors holds a list of selectors which will be used to find ClusterRoles and create the rules. If any of the selectors match, then the ClusterRole's permissions will be added",
    )


class ClusterRole(BaseModel):
    aggregationRule: Optional[AggregationRule] = Field(
        None,
        description='AggregationRule is an optional field that describes how to build the Rules for this ClusterRole. If AggregationRule is set, then the Rules are controller managed and direct changes to Rules will be stomped by the controller.',
    )
    apiVersion: Optional[str] = Field(
        None,
        description='APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources',
    )
    kind: Optional[Kind123] = Field(
        None,
        description='Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds',
    )
    metadata: Optional[v1.ObjectMeta] = Field(
        None, description="Standard object's metadata."
    )
    rules: Optional[List[PolicyRule]] = Field(
        None, description='Rules holds all the PolicyRules for this ClusterRole'
    )


class ClusterRoleBinding(BaseModel):
    apiVersion: Optional[str] = Field(
        None,
        description='APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources',
    )
    kind: Optional[Kind124] = Field(
        None,
        description='Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds',
    )
    metadata: Optional[v1.ObjectMeta] = Field(
        None, description="Standard object's metadata."
    )
    roleRef: RoleRef = Field(
        ...,
        description='RoleRef can only reference a ClusterRole in the global namespace. If the RoleRef cannot be resolved, the Authorizer must return an error.',
    )
    subjects: Optional[List[Subject]] = Field(
        None,
        description='Subjects holds references to the objects the role applies to.',
    )


class ClusterRoleBindingList(BaseModel):
    apiVersion: Optional[str] = Field(
        None,
        description='APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources',
    )
    items: List[ClusterRoleBinding] = Field(
        ..., description='Items is a list of ClusterRoleBindings'
    )
    kind: Optional[Kind125] = Field(
        None,
        description='Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds',
    )
    metadata: Optional[v1.ListMeta] = Field(
        None, description="Standard object's metadata."
    )


class ClusterRoleList(BaseModel):
    apiVersion: Optional[str] = Field(
        None,
        description='APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources',
    )
    items: List[ClusterRole] = Field(..., description='Items is a list of ClusterRoles')
    kind: Optional[Kind126] = Field(
        None,
        description='Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds',
    )
    metadata: Optional[v1.ListMeta] = Field(
        None, description="Standard object's metadata."
    )


class Role(BaseModel):
    apiVersion: Optional[str] = Field(
        None,
        description='APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources',
    )
    kind: Optional[Kind127] = Field(
        None,
        description='Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds',
    )
    metadata: Optional[v1.ObjectMeta] = Field(
        None, description="Standard object's metadata."
    )
    rules: Optional[List[PolicyRule]] = Field(
        None, description='Rules holds all the PolicyRules for this Role'
    )


class RoleBinding(BaseModel):
    apiVersion: Optional[str] = Field(
        None,
        description='APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources',
    )
    kind: Optional[Kind128] = Field(
        None,
        description='Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds',
    )
    metadata: Optional[v1.ObjectMeta] = Field(
        None, description="Standard object's metadata."
    )
    roleRef: RoleRef = Field(
        ...,
        description='RoleRef can reference a Role in the current namespace or a ClusterRole in the global namespace. If the RoleRef cannot be resolved, the Authorizer must return an error.',
    )
    subjects: Optional[List[Subject]] = Field(
        None,
        description='Subjects holds references to the objects the role applies to.',
    )


class RoleBindingList(BaseModel):
    apiVersion: Optional[str] = Field(
        None,
        description='APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources',
    )
    items: List[RoleBinding] = Field(..., description='Items is a list of RoleBindings')
    kind: Optional[Kind129] = Field(
        None,
        description='Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds',
    )
    metadata: Optional[v1.ListMeta] = Field(
        None, description="Standard object's metadata."
    )


class RoleList(BaseModel):
    apiVersion: Optional[str] = Field(
        None,
        description='APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources',
    )
    items: List[Role] = Field(..., description='Items is a list of Roles')
    kind: Optional[Kind130] = Field(
        None,
        description='Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds',
    )
    metadata: Optional[v1.ListMeta] = Field(
        None, description="Standard object's metadata."
    )
