// Copyright 2019 Polyaxon, Inc.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

// Code generated by go-swagger; DO NOT EDIT.

package service_client

// This file was generated by the swagger tool.
// Editing this file might prove futile when you re-run the swagger generate command

import (
	"github.com/go-openapi/runtime"
	httptransport "github.com/go-openapi/runtime/client"

	strfmt "github.com/go-openapi/strfmt"

	"github.com/polyaxon/polyaxon/sdks/go/http_client/v1/service_client/agents_v1"
	"github.com/polyaxon/polyaxon/sdks/go/http_client/v1/service_client/artifacts_stores_v1"
	"github.com/polyaxon/polyaxon/sdks/go/http_client/v1/service_client/auth_v1"
	"github.com/polyaxon/polyaxon/sdks/go/http_client/v1/service_client/config_resources_v1"
	"github.com/polyaxon/polyaxon/sdks/go/http_client/v1/service_client/connections_v1"
	"github.com/polyaxon/polyaxon/sdks/go/http_client/v1/service_client/dashboards_v1"
	"github.com/polyaxon/polyaxon/sdks/go/http_client/v1/service_client/organizations_v1"
	"github.com/polyaxon/polyaxon/sdks/go/http_client/v1/service_client/project_dashboards_v1"
	"github.com/polyaxon/polyaxon/sdks/go/http_client/v1/service_client/project_searches_v1"
	"github.com/polyaxon/polyaxon/sdks/go/http_client/v1/service_client/projects_v1"
	"github.com/polyaxon/polyaxon/sdks/go/http_client/v1/service_client/queues_v1"
	"github.com/polyaxon/polyaxon/sdks/go/http_client/v1/service_client/run_profiles_v1"
	"github.com/polyaxon/polyaxon/sdks/go/http_client/v1/service_client/runs_v1"
	"github.com/polyaxon/polyaxon/sdks/go/http_client/v1/service_client/schemas_v1"
	"github.com/polyaxon/polyaxon/sdks/go/http_client/v1/service_client/searches_v1"
	"github.com/polyaxon/polyaxon/sdks/go/http_client/v1/service_client/teams_v1"
	"github.com/polyaxon/polyaxon/sdks/go/http_client/v1/service_client/users_v1"
	"github.com/polyaxon/polyaxon/sdks/go/http_client/v1/service_client/versions_v1"
)

// Default polyaxon sdk HTTP client.
var Default = NewHTTPClient(nil)

const (
	// DefaultHost is the default Host
	// found in Meta (info) section of spec file
	DefaultHost string = "localhost"
	// DefaultBasePath is the default BasePath
	// found in Meta (info) section of spec file
	DefaultBasePath string = "/"
)

// DefaultSchemes are the default schemes found in Meta (info) section of spec file
var DefaultSchemes = []string{"http", "https"}

// NewHTTPClient creates a new polyaxon sdk HTTP client.
func NewHTTPClient(formats strfmt.Registry) *PolyaxonSdk {
	return NewHTTPClientWithConfig(formats, nil)
}

// NewHTTPClientWithConfig creates a new polyaxon sdk HTTP client,
// using a customizable transport config.
func NewHTTPClientWithConfig(formats strfmt.Registry, cfg *TransportConfig) *PolyaxonSdk {
	// ensure nullable parameters have default
	if cfg == nil {
		cfg = DefaultTransportConfig()
	}

	// create transport and client
	transport := httptransport.New(cfg.Host, cfg.BasePath, cfg.Schemes)
	return New(transport, formats)
}

// New creates a new polyaxon sdk client
func New(transport runtime.ClientTransport, formats strfmt.Registry) *PolyaxonSdk {
	// ensure nullable parameters have default
	if formats == nil {
		formats = strfmt.Default
	}

	cli := new(PolyaxonSdk)
	cli.Transport = transport

	cli.AgentsV1 = agents_v1.New(transport, formats)

	cli.ArtifactsStoresV1 = artifacts_stores_v1.New(transport, formats)

	cli.AuthV1 = auth_v1.New(transport, formats)

	cli.ConfigResourcesV1 = config_resources_v1.New(transport, formats)

	cli.ConnectionsV1 = connections_v1.New(transport, formats)

	cli.DashboardsV1 = dashboards_v1.New(transport, formats)

	cli.OrganizationsV1 = organizations_v1.New(transport, formats)

	cli.ProjectDashboardsV1 = project_dashboards_v1.New(transport, formats)

	cli.ProjectSearchesV1 = project_searches_v1.New(transport, formats)

	cli.ProjectsV1 = projects_v1.New(transport, formats)

	cli.QueuesV1 = queues_v1.New(transport, formats)

	cli.RunProfilesV1 = run_profiles_v1.New(transport, formats)

	cli.RunsV1 = runs_v1.New(transport, formats)

	cli.SchemasV1 = schemas_v1.New(transport, formats)

	cli.SearchesV1 = searches_v1.New(transport, formats)

	cli.TeamsV1 = teams_v1.New(transport, formats)

	cli.UsersV1 = users_v1.New(transport, formats)

	cli.VersionsV1 = versions_v1.New(transport, formats)

	return cli
}

// DefaultTransportConfig creates a TransportConfig with the
// default settings taken from the meta section of the spec file.
func DefaultTransportConfig() *TransportConfig {
	return &TransportConfig{
		Host:     DefaultHost,
		BasePath: DefaultBasePath,
		Schemes:  DefaultSchemes,
	}
}

// TransportConfig contains the transport related info,
// found in the meta section of the spec file.
type TransportConfig struct {
	Host     string
	BasePath string
	Schemes  []string
}

// WithHost overrides the default host,
// provided by the meta section of the spec file.
func (cfg *TransportConfig) WithHost(host string) *TransportConfig {
	cfg.Host = host
	return cfg
}

// WithBasePath overrides the default basePath,
// provided by the meta section of the spec file.
func (cfg *TransportConfig) WithBasePath(basePath string) *TransportConfig {
	cfg.BasePath = basePath
	return cfg
}

// WithSchemes overrides the default schemes,
// provided by the meta section of the spec file.
func (cfg *TransportConfig) WithSchemes(schemes []string) *TransportConfig {
	cfg.Schemes = schemes
	return cfg
}

// PolyaxonSdk is a client for polyaxon sdk
type PolyaxonSdk struct {
	AgentsV1 *agents_v1.Client

	ArtifactsStoresV1 *artifacts_stores_v1.Client

	AuthV1 *auth_v1.Client

	ConfigResourcesV1 *config_resources_v1.Client

	ConnectionsV1 *connections_v1.Client

	DashboardsV1 *dashboards_v1.Client

	OrganizationsV1 *organizations_v1.Client

	ProjectDashboardsV1 *project_dashboards_v1.Client

	ProjectSearchesV1 *project_searches_v1.Client

	ProjectsV1 *projects_v1.Client

	QueuesV1 *queues_v1.Client

	RunProfilesV1 *run_profiles_v1.Client

	RunsV1 *runs_v1.Client

	SchemasV1 *schemas_v1.Client

	SearchesV1 *searches_v1.Client

	TeamsV1 *teams_v1.Client

	UsersV1 *users_v1.Client

	VersionsV1 *versions_v1.Client

	Transport runtime.ClientTransport
}

// SetTransport changes the transport on the client and all its subresources
func (c *PolyaxonSdk) SetTransport(transport runtime.ClientTransport) {
	c.Transport = transport

	c.AgentsV1.SetTransport(transport)

	c.ArtifactsStoresV1.SetTransport(transport)

	c.AuthV1.SetTransport(transport)

	c.ConfigResourcesV1.SetTransport(transport)

	c.ConnectionsV1.SetTransport(transport)

	c.DashboardsV1.SetTransport(transport)

	c.OrganizationsV1.SetTransport(transport)

	c.ProjectDashboardsV1.SetTransport(transport)

	c.ProjectSearchesV1.SetTransport(transport)

	c.ProjectsV1.SetTransport(transport)

	c.QueuesV1.SetTransport(transport)

	c.RunProfilesV1.SetTransport(transport)

	c.RunsV1.SetTransport(transport)

	c.SchemasV1.SetTransport(transport)

	c.SearchesV1.SetTransport(transport)

	c.TeamsV1.SetTransport(transport)

	c.UsersV1.SetTransport(transport)

	c.VersionsV1.SetTransport(transport)

}
