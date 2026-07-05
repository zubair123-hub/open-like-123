# REST API Documentation

Complete REST API reference for Offline Pentesting AI.

## Base URL

```
http://localhost:8000
```

---

## Endpoints

### Health & Status

#### GET `/`
Get API status.

**Response:**
```json
{
  "status": "ok",
  "version": "1.0.0",
  "timestamp": "2024-01-15T10:30:45Z"
}
```

#### GET `/health`
Health check endpoint.

**Response:**
```json
{
  "status": "healthy",
  "uptime": "2h 30m",
  "services": {
    "database": "connected",
    "ollama": "connected",
    "cache": "connected"
  }
}
```

---

### Tools

#### GET `/api/tools`
List all available security tools.

**Response:**
```json
{
  "tools": [
    {
      "name": "nmap",
      "installed": true,
      "description": "Network mapper for security scanning",
      "default_args": ["-sV", "-sC"]
    },
    {
      "name": "curl",
      "installed": true,
      "description": "Transfer data using URLs",
      "default_args": ["-I", "-L"]
    }
  ]
}
```

#### GET `/api/tools/{tool_name}`
Get details of a specific tool.

**Response:**
```json
{
  "name": "nmap",
  "installed": true,
  "description": "Network mapper",
  "command": "nmap",
  "args": ["-sV", "-sC"],
  "last_used": "2024-01-15T09:15:00Z"
}
```

---

### Scans

#### POST `/api/scan`
Start a new security scan.

**Request:**
```json
{
  "target": "example.com",
  "scan_type": "quick",
  "tools": ["nmap", "curl", "dig"],
  "timeout": 300,
  "async": true
}
```

**Parameters:**
- `target` (string, required) - Target URL or IP address
- `scan_type` (string) - `quick`, `full`, or `custom` (default: `quick`)
- `tools` (array) - Specific tools to run (optional)
- `timeout` (integer) - Scan timeout in seconds (default: 300)
- `async` (boolean) - Run asynchronously (default: true)

**Response:**
```json
{
  "scan_id": "scan_abc123",
  "target": "example.com",
  "status": "queued",
  "created_at": "2024-01-15T10:30:45Z",
  "estimated_duration": "120s"
}
```

#### GET `/api/scan/{scan_id}`
Get scan status and results.

**Response:**
```json
{
  "scan_id": "scan_abc123",
  "target": "example.com",
  "status": "running",
  "progress": 45,
  "started_at": "2024-01-15T10:30:45Z",
  "elapsed_time": "60s",
  "estimated_remaining": "60s",
  "results": {
    "nmap": {
      "stdout": "...",
      "stderr": "",
      "returncode": 0
    }
  }
}
```

**Status Values:**
- `queued` - Waiting to start
- `running` - Currently executing
- `completed` - Finished successfully
- `failed` - Execution failed
- `cancelled` - User cancelled

#### GET `/api/scans`
List all scans.

**Query Parameters:**
- `limit` (integer) - Results per page (default: 30, max: 100)
- `offset` (integer) - Results offset (default: 0)
- `status` (string) - Filter by status
- `target` (string) - Filter by target

**Response:**
```json
{
  "scans": [
    {
      "scan_id": "scan_abc123",
      "target": "example.com",
      "status": "completed",
      "created_at": "2024-01-15T10:30:45Z"
    }
  ],
  "total": 150,
  "limit": 30,
  "offset": 0
}
```

#### DELETE `/api/scan/{scan_id}`
Cancel a running scan.

**Response:**
```json
{
  "scan_id": "scan_abc123",
  "status": "cancelled",
  "message": "Scan cancelled successfully"
}
```

---

### Reports

#### GET `/api/reports`
List all generated reports.

**Query Parameters:**
- `limit` (integer) - Results per page
- `offset` (integer) - Results offset
- `format` (string) - Filter by format (html, pdf, json)
- `scan_id` (string) - Filter by scan ID

**Response:**
```json
{
  "reports": [
    {
      "report_id": "rep_001",
      "scan_id": "scan_abc123",
      "format": "html",
      "created_at": "2024-01-15T11:00:00Z",
      "size": "2.5MB",
      "url": "/api/reports/rep_001/download"
    }
  ],
  "total": 42
}
```

#### POST `/api/reports`
Generate a new report from a scan.

**Request:**
```json
{
  "scan_id": "scan_abc123",
  "formats": ["html", "pdf", "json"],
  "include_evidence": true
}
```

**Response:**
```json
{
  "report_id": "rep_001",
  "scan_id": "scan_abc123",
  "status": "generating",
  "formats": ["html", "pdf", "json"]
}
```

#### GET `/api/reports/{report_id}`
Get report metadata.

**Response:**
```json
{
  "report_id": "rep_001",
  "scan_id": "scan_abc123",
  "formats": ["html", "pdf", "json"],
  "created_at": "2024-01-15T11:00:00Z",
  "status": "completed",
  "file_sizes": {
    "html": "2.5MB",
    "pdf": "3.1MB",
    "json": "1.2MB"
  }
}
```

#### GET `/api/reports/{report_id}/download?format={format}`
Download a report.

**Parameters:**
- `format` (string) - html, pdf, or json

**Response:**
- Binary file content
- Content-Type: application/pdf, text/html, or application/json
- Content-Disposition: attachment

---

### AI & Reasoning

#### POST `/api/ai/plan`
Get AI-generated pentesting plan for a target.

**Request:**
```json
{
  "target": "example.com",
  "context": "Website assessment",
  "scope": ["reconnaissance", "scanning", "enumeration"]
}
```

**Response:**
```json
{
  "plan_id": "plan_xyz",
  "phases": [
    {
      "phase": 1,
      "name": "Reconnaissance",
      "tools": ["whois", "dig", "nmap"],
      "description": "Initial information gathering..."
    },
    {
      "phase": 2,
      "name": "Scanning",
      "tools": ["nmap", "ssl-scan"],
      "description": "Active scanning for vulnerabilities..."
    }
  ],
  "estimated_duration": "2h 30m"
}
```

#### GET `/api/ai/insights/{scan_id}`
Get AI insights from a completed scan.

**Response:**
```json
{
  "scan_id": "scan_abc123",
  "insights": {
    "summary": "Open ports discovered on target...",
    "critical_findings": [...],
    "recommendations": [...],
    "severity_breakdown": {
      "critical": 1,
      "high": 3,
      "medium": 5,
      "low": 2
    }
  }
}
```

---

### Configuration

#### GET `/api/config`
Get current configuration (non-sensitive values only).

**Response:**
```json
{
  "debug": false,
  "log_level": "INFO",
  "api_port": 8000,
  "ollama_model": "mistral",
  "max_concurrent_scans": 5,
  "default_timeout": 300
}
```

#### GET `/api/config/models`
List configured LLM models.

**Response:**
```json
{
  "current_model": "mistral",
  "available_models": [
    {
      "name": "mistral",
      "size": "7.3GB",
      "installed": true
    },
    {
      "name": "llama2",
      "size": "3.8GB",
      "installed": false
    }
  ]
}
```

---

## Error Responses

### 400 Bad Request
```json
{
  "error": "Invalid request",
  "message": "Missing required parameter: target",
  "code": "MISSING_PARAMETER"
}
```

### 404 Not Found
```json
{
  "error": "Not found",
  "message": "Scan with ID 'scan_invalid' not found",
  "code": "NOT_FOUND"
}
```

### 429 Too Many Requests
```json
{
  "error": "Rate limited",
  "message": "Too many requests. Please wait before trying again.",
  "code": "RATE_LIMIT_EXCEEDED",
  "retry_after": 60
}
```

### 500 Internal Server Error
```json
{
  "error": "Internal server error",
  "message": "An unexpected error occurred",
  "code": "INTERNAL_ERROR",
  "request_id": "req_12345"
}
```

---

## Authentication

### API Key Authentication (Future)

```bash
curl -H "Authorization: Bearer YOUR_API_KEY" \
  http://localhost:8000/api/scan
```

---

## Rate Limiting

- **Requests per minute**: 60
- **Concurrent scans**: 5
- **Max scan duration**: 30 minutes

---

## Examples

### Example 1: Quick Scan
```bash
curl -X POST http://localhost:8000/api/scan \
  -H "Content-Type: application/json" \
  -d '{
    "target": "example.com",
    "scan_type": "quick"
  }'
```

### Example 2: Check Scan Status
```bash
curl http://localhost:8000/api/scan/scan_abc123
```

### Example 3: Generate Report
```bash
curl -X POST http://localhost:8000/api/reports \
  -H "Content-Type: application/json" \
  -d '{
    "scan_id": "scan_abc123",
    "formats": ["html", "pdf"]
  }'
```

### Example 4: Get AI Insights
```bash
curl http://localhost:8000/api/ai/insights/scan_abc123
```

---

## WebSocket Events (Real-time Updates)

Connect to `/ws` for real-time scan updates:

```javascript
const ws = new WebSocket('ws://localhost:8000/ws');

ws.onmessage = (event) => {
  const data = JSON.parse(event.data);
  console.log(data);
  // {
  //   "type": "scan_progress",
  //   "scan_id": "scan_abc123",
  //   "progress": 45,
  //   "current_tool": "nmap",
  //   "message": "Running nmap scan..."
  // }
};
```

---

## SDK / Client Libraries

### Python
```python
from api_client import PentestingAIClient

client = PentestingAIClient('http://localhost:8000')

# Start scan
scan = client.start_scan('example.com', scan_type='quick')

# Check status
status = client.get_scan_status(scan.id)

# Generate report
report = client.generate_report(scan.id, formats=['html', 'pdf'])
```

### JavaScript/TypeScript
```typescript
import { PentestingAIClient } from 'pentesting-ai-client';

const client = new PentestingAIClient('http://localhost:8000');

// Start scan
const scan = await client.startScan('example.com', { scanType: 'quick' });

// Check status
const status = await client.getScanStatus(scan.id);

// Generate report
const report = await client.generateReport(scan.id, ['html', 'pdf']);
```

---

## Rate Limit Headers

All responses include:
```
X-RateLimit-Limit: 60
X-RateLimit-Remaining: 59
X-RateLimit-Reset: 1705317045
```

---

For more information, see [README.md](../README.md) or contact support.
