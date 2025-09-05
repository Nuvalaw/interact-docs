# Integration Overview

This page explains how to integrate your claims management system with the Nuvalaw Interact platform.

## Purpose of Integration

Integration allows data to flow automatically between your system and Nuvalaw. The main objectives are:

- Reduce duplicate data entry  
- Keep claims, documents, and statuses synchronized  
- Provide faster access to case information  

## Integration Methods

Nuvalaw supports two integration approaches. The choice depends on your system capabilities and security requirements.

### REST API (recommended)

- Real-time integration  
- Data format: JSON  
- Secure document upload supported  
- Authentication: OAuth2 or API keys  

### Secure File Transfer Protocol (SFTP)

- Suitable where APIs are not available  
- Data format: encrypted CSV files  
- Exchange via secure SFTP server  
- Authentication: key-based  

## Data Flow

The integration is configured during the discovery phase. The typical flows are:

**Inbound to Nuvalaw**

  - Claim and party data  
  - Supporting documents (PDF, image, correspondence)  
  - Any information required for arbitration  

**Outbound to your system**

  - Claim status updates  
  - Award or settlement details  
  - Generated documents  
  - Audit trail data  

## Implementation Process

Integration follows a structured process. Timelines are confirmed during discovery.

1. **Discovery and mapping** — confirm systems, data, and scope  
2. **Build and test** — implement and verify the integration  
3. **User Acceptance Testing (UAT)** — validate integration with your team  
4. **Go-live** — deploy the integration to production  

## Security

All integrations apply standard enterprise security practices:

- Data in transit: TLS/HTTPS  
- Data at rest: encrypted storage  
- Authentication: OAuth2, API keys, or SFTP keys  
- Access control: role-based permissions  
- Audit logging: full record of actions  

If your organisation wishes to learn more, please email {{ support }}.
