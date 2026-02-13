# 🚨 Production Issues & Troubleshooting Guide

**Purpose**: Document common production issues, debugging approaches, and prevention strategies as you learn.

**How to Use**: Fill this in throughout your 24-week journey. Every time you encounter an error, debug an issue, or learn about a production problem, add it here.

---

## 📖 Table of Contents

1. [Core Java Issues](#core-java-issues)
2. [Spring Boot Issues](#spring-boot-issues)
3. [Database Issues](#database-issues)
4. [Microservices Issues](#microservices-issues)
5. [Docker Issues](#docker-issues)
6. [Kubernetes Issues](#kubernetes-issues)
7. [Golang Issues](#golang-issues)
8. [General Debugging Approaches](#general-debugging-approaches)
9. [Monitoring & Observability](#monitoring--observability)
10. [Incident Response Process](#incident-response-process)

---

## 🔧 Core Java Issues

### Memory Issues

#### OutOfMemoryError

**Cause**:

- Heap memory exhausted
- Memory leaks (objects not garbage collected)
- Large objects loaded into memory

**Symptoms**:

```
java.lang.OutOfMemoryError: Java heap space
```

**Debug**:

- Check heap usage: `jmap -heap <pid>`
- Heap dump: `jmap -dump:live,format=b,file=heap.bin <pid>`
- Analyze with VisualVM or Eclipse MAT

**Prevention**:

- Set appropriate heap size: `-Xmx2g -Xms1g`
- Use streaming for large data
- Close resources properly
- Profile memory usage

**Example Scenario**:

```java
// Bad: Loading entire file into memory
List<String> lines = Files.readAllLines(Path.of("large.txt"));

// Good: Stream processing
try (Stream<String> lines = Files.lines(Path.of("large.txt"))) {
    lines.forEach(line -> process(line));
}
```

**My Experience**:

```
[Date: ________]
Issue:
How I debugged it:
Solution:
What I learned:
```

---

#### StackOverflowError

**Cause**:

- Infinite recursion
- Very deep recursion without base case
- Stack size too small

**Symptoms**:

```
java.lang.StackOverflowError
```

**Debug**:

- Check stack trace for repeating method calls
- Review recursive logic

**Prevention**:

- Always have base case in recursion
- Consider iterative alternatives
- Increase stack size if needed: `-Xss2m`

**My Experience**:

```
[Date: ________]
Issue:
Solution:
```

---

### Thread Issues

#### Deadlock

**Cause**:

- Two threads waiting for each other's locks
- Circular dependency in lock acquisition

**Symptoms**:

- Application hangs
- No CPU usage but no progress

**Debug**:

- Thread dump: `jstack <pid>`
- Look for "waiting to lock" and "locked" patterns

**Prevention**:

- Always acquire locks in same order
- Use timeout on lock acquisition
- Prefer higher-level concurrency utilities

**Example**:

```java
// Bad: Potential deadlock
synchronized(lockA) {
    synchronized(lockB) {
        // ...
    }
}

// Good: Use Lock with tryLock
if (lockA.tryLock(1, TimeUnit.SECONDS)) {
    try {
        if (lockB.tryLock(1, TimeUnit.SECONDS)) {
            try {
                // Do work
            } finally {
                lockB.unlock();
            }
        }
    } finally {
        lockA.unlock();
    }
}
```

**My Experience**:

```
[Date: ________]
```

---

## 🍃 Spring Boot Issues

### Application Startup Issues

#### Port Already in Use

**Symptoms**:

```
Web server failed to start. Port 8080 was already in use.
```

**Debug**:

- Check running processes: `netstat -ano | findstr :8080`
- Kill process or change port

**Prevention**:

- Use different ports for different apps
- Configure in `application.properties`: `server.port=8081`

**My Experience**:

```
[Date: ________]
```

---

#### DataSource Connection Failed

**Cause**:

- Database not running
- Wrong credentials
- Network issues

**Symptoms**:

```
Failed to configure a DataSource
Cannot create PoolableConnectionFactory
```

**Debug**:

- Verify DB is running
- Check connection string
- Test connection manually
- Check credentials

**Prevention**:

- Use health checks
- Connection pool monitoring
- Proper error messages

**Example Config**:

```properties
spring.datasource.url=jdbc:postgresql://localhost:5432/mydb
spring.datasource.username=user
spring.datasource.password=pass

# Connection pool settings
spring.datasource.hikari.maximum-pool-size=10
spring.datasource.hikari.connection-timeout=30000
```

**My Experience**:

```
[Date: ________]
```

---

### API Issues

#### 500 Internal Server Error

**Common Causes**:

- Unhandled exceptions
- NullPointerException
- Database query failed
- External service timeout

**Debug**:

1. Check application logs
2. Look for stack trace
3. Check request parameters
4. Verify DB connection

**Prevention**:

- Global exception handler (`@ControllerAdvice`)
- Proper validation
- Null checks
- Defensive programming

**Example**:

```java
@ControllerAdvice
public class GlobalExceptionHandler {

    @ExceptionHandler(ResourceNotFoundException.class)
    public ResponseEntity<ErrorResponse> handleNotFound(ResourceNotFoundException ex) {
        log.error("Resource not found: {}", ex.getMessage());
        return ResponseEntity.status(HttpStatus.NOT_FOUND)
            .body(new ErrorResponse(ex.getMessage()));
    }

    @ExceptionHandler(Exception.class)
    public ResponseEntity<ErrorResponse> handleGeneral(Exception ex) {
        log.error("Unexpected error", ex);
        return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR)
            .body(new ErrorResponse("Internal server error"));
    }
}
```

**My Experience**:

```
[Date: ________]
```

---

#### Slow API Response

**Common Causes**:

- N+1 query problem
- Missing database indexes
- Synchronous external API calls
- Large data fetching

**Debug**:

- Check response time in logs
- Enable SQL logging
- Use APM tools
- Profile the code

**Prevention**:

- Use JPA fetch strategies wisely
- Add database indexes
- Async processing for long tasks
- Pagination for large datasets
- Caching

**My Experience**:

```
[Date: ________]
```

---

## 🗄️ Database Issues

### Connection Pool Exhausted

**Cause**:

- Not closing connections
- Too many concurrent requests
- Connection leak
- Pool size too small

**Symptoms**:

```
Cannot get JDBC Connection
Pool is exhausted
```

**Debug**:

- Check active connections
- Review connection pool metrics
- Look for unclosed connections in code

**Prevention**:

```java
// Bad: Connection leak
Connection conn = dataSource.getConnection();
// ... forgot to close

// Good: Auto-close
try (Connection conn = dataSource.getConnection()) {
    // Use connection
} // Automatically closed
```

**My Experience**:

```
[Date: ________]
```

---

### Slow Queries

**Cause**:

- Missing indexes
- Large table scans
- Complex joins
- Inefficient queries

**Debug**:

- Enable SQL logging
- Use EXPLAIN ANALYZE
- Check query execution plan
- Monitor query time

**Prevention**:

- Add appropriate indexes
- Optimize queries
- Use pagination
- Consider caching

**My Experience**:

```
[Date: ________]
```

---

## 🔀 Microservices Issues

### Service Discovery Failures

**Cause**:

- Service not registered
- Eureka/Consul down
- Network issues

**Symptoms**:

- Cannot find service
- LoadBalancer errors

**Debug**:

- Check service registry UI
- Verify service registration
- Check network connectivity

**Prevention**:

- Health checks
- Retry logic
- Fallback mechanisms

**My Experience**:

```
[Date: ________]
```

---

### Circuit Breaker Opened

**Cause**:

- Too many failures
- Downstream service down
- Timeout threshold exceeded

**Symptoms**:

- Circuit open errors
- Fallback responses returned

**Debug**:

- Check circuit breaker metrics
- Review downstream service health
- Check timeout settings

**Prevention**:

- Proper timeout configuration
- Gradual degradation
- Monitor downstream services

**My Experience**:

```
[Date: ________]
```

---

### Distributed Transaction Failures

**Cause**:

- Network partition
- Service crash mid-transaction
- Timeout

**Debug**:

- Check saga/transaction logs
- Verify compensating transactions
- Review rollback logic

**Prevention**:

- Saga pattern
- Idempotency
- Event sourcing
- Proper error handling

**My Experience**:

```
[Date: ________]
```

---

## 🐳 Docker Issues

### Container Keeps Restarting

**Cause**:

- Application crash on startup
- Health check failing
- Port conflict
- Memory limit exceeded

**Debug**:

```bash
# Check container logs
docker logs <container-id>

# Check last 50 lines
docker logs --tail 50 <container-id>

# Follow logs
docker logs -f <container-id>

# Check container status
docker ps -a

# Inspect container
docker inspect <container-id>
```

**Prevention**:

- Proper health checks
- Adequate resource limits
- Graceful shutdown handling

**My Experience**:

```
[Date: ________]
```

---

### ImagePullBackOff

**Cause**:

- Image doesn't exist
- Registry authentication failed
- Network issues

**Debug**:

```bash
# Check events
docker events

# Verify image exists
docker pull <image-name>

# Check registry credentials
docker login
```

**Prevention**:

- Verify image names
- Proper registry authentication
- Use image digests

**My Experience**:

```
[Date: ________]
```

---

### Out of Disk Space

**Cause**:

- Too many unused images
- Large containers
- Volume data accumulation

**Debug**:

```bash
# Check disk usage
docker system df

# See all images
docker images

# See dangling images
docker images -f dangling=true
```

**Prevention**:

```bash
# Cleanup
docker system prune -a

# Remove unused volumes
docker volume prune

# Scheduled cleanup
```

**My Experience**:

```
[Date: ________]
```

---

## ☸️ Kubernetes Issues

### Pod Stuck in Pending

**Cause**:

- Insufficient resources
- No nodes available
- Volume mount issues
- Image pull errors

**Debug**:

```bash
# Describe pod
kubectl describe pod <pod-name>

# Check events
kubectl get events --sort-by='.lastTimestamp'

# Check node resources
kubectl top nodes
```

**Prevention**:

- Set resource requests/limits
- Check cluster capacity
- Verify PVC exists

**My Experience**:

```
[Date: ________]
```

---

### CrashLoopBackOff

**Cause**:

- Application crash on startup
- Failed liveness probe
- Missing configuration
- Database not ready

**Debug**:

```bash
# Check pod logs
kubectl logs <pod-name>

# Previous container logs
kubectl logs <pod-name> --previous

# Describe pod
kubectl describe pod <pod-name>
```

**Prevention**:

- Init containers for dependencies
- Proper readiness probes
- Configuration validation
- Dependency checks

**My Experience**:

```
[Date: ________]
```

---

### OOMKilled

**Cause**:

- Memory limit too low
- Memory leak
- Large data processing

**Symptoms**:

```
Last State: Terminated
Reason: OOMKilled
Exit Code: 137
```

**Debug**:

```bash
# Check pod memory usage
kubectl top pod <pod-name>

# Check memory limits
kubectl describe pod <pod-name> | grep -i memory
```

**Prevention**:

- Increase memory limits
- Fix memory leaks
- Optimize application

**Example**:

```yaml
resources:
  requests:
    memory: "256Mi"
  limits:
    memory: "512Mi"
```

**My Experience**:

```
[Date: ________]
```

---

### Service Not Accessible

**Cause**:

- Wrong service type
- Pod selector mismatch
- Network policy blocking
- Port mismatch

**Debug**:

```bash
# Check service
kubectl get svc

# Describe service
kubectl describe svc <service-name>

# Check endpoints
kubectl get endpoints <service-name>

# Check pods with label
kubectl get pods -l app=myapp
```

**Prevention**:

- Verify labels match
- Check port configuration
- Test internal connectivity

**My Experience**:

```
[Date: ________]
```

---

## 🐹 Golang Issues

### Goroutine Leaks

**Cause**:

- Goroutines not terminating
- Blocked channel operations
- Missing context cancellation

**Debug**:

- Use pprof for goroutine profiling
- Check goroutine count over time

**Prevention**:

- Always use context
- Ensure goroutines can exit
- Use timeouts

**My Experience**:

```
[Date: ________]
```

---

### Race Conditions

**Cause**:

- Concurrent map access
- Shared variable access without sync

**Debug**:

```bash
go run -race main.go
```

**Prevention**:

- Use sync.Mutex
- Use channels
- sync.Map for concurrent maps

**My Experience**:

```
[Date: ________]
```

---

## 🔍 General Debugging Approaches

### The 5-Step Debug Process

1. **Reproduce the Issue**
   - Understand exact steps
   - Note environment details
   - Check if consistent

2. **Gather Information**
   - Application logs
   - System metrics (CPU, memory, disk)
   - Network traffic
   - Database queries
   - Recent changes

3. **Form Hypothesis**
   - What could cause this?
   - Has this happened before?
   - What changed recently?

4. **Test Hypothesis**
   - Add logging
   - Use debugger
   - Check metrics
   - Review code

5. **Fix and Verify**
   - Implement fix
   - Test thoroughly
   - Monitor in production
   - Document for future

---

### Debugging Commands Cheat Sheet

#### Java/Spring Boot

```bash
# Check Java processes
jps

# Thread dump
jstack <pid>

# Heap dump
jmap -dump:live,format=b,file=heap.bin <pid>

# GC logs
-XX:+PrintGCDetails -XX:+PrintGCDateStamps
```

#### Docker

```bash
# Logs
docker logs <container>

# Execute command
docker exec -it <container> bash

# Copy files
docker cp <container>:/path/file ./local

# Stats
docker stats
```

#### Kubernetes

```bash
# Logs
kubectl logs <pod>

# Exec into pod
kubectl exec -it <pod> -- bash

# Port forward
kubectl port-forward <pod> 8080:8080

# Describe
kubectl describe pod <pod>
```

---

## 📊 Monitoring & Observability

### Key Metrics to Monitor

#### Application Metrics

- [ ] Request rate
- [ ] Error rate
- [ ] Response time (p50, p95, p99)
- [ ] Active connections
- [ ] Thread pool usage

#### System Metrics

- [ ] CPU usage
- [ ] Memory usage
- [ ] Disk I/O
- [ ] Network I/O

#### Database Metrics

- [ ] Query time
- [ ] Connection pool usage
- [ ] Slow query count
- [ ] Lock waits

### Logging Best Practices

```java
// Bad
System.out.println("Error");

// Good
log.error("Failed to process order: orderId={}, userId={}, error={}",
          orderId, userId, e.getMessage(), e);
```

**Log Levels**:

- **ERROR**: System errors, exceptions
- **WARN**: Potential issues
- **INFO**: Important business events
- **DEBUG**: Detailed diagnostic info

**My Monitoring Setup**:

```
[Date: ________]
Tools used:
Dashboards created:
Alerts configured:
```

---

## 🚨 Incident Response Process

### During an Incident

1. **Acknowledge**
   - Acknowledge the alert
   - Form incident team

2. **Assess**
   - What's the impact?
   - How many users affected?
   - Is it critical?

3. **Communicate**
   - Notify stakeholders
   - Update status page
   - Regular updates

4. **Mitigate**
   - Rollback if needed
   - Scale up resources
   - Disable problematic feature
   - Apply hotfix

5. **Resolve**
   - Verify fix
   - Monitor closely
   - All clear

6. **Post-Mortem**
   - What happened?
   - Root cause?
   - How to prevent?
   - Action items

### My Incident Log

```
[Date: ________]
Incident:
Impact:
Root Cause:
Resolution:
Prevention:
Lessons Learned:

---

[Date: ________]
Incident:
...
```

---

## 📝 Daily Learning Log

**Use this section to log errors you encounter during your 24-week journey**

### Week 1-4 (Core Java)

```
[Date: ________]
Error:
What I learned:

[Date: ________]
Error:
What I learned:
```

### Week 5-9 (Spring Boot)

```
[Date: ________]
Error:
What I learned:
```

### Week 10-12 (Microservices)

```
[Date: ________]
Error:
What I learned:
```

### Week 13-16 (Docker/K8s)

```
[Date: ________]
Error:
What I learned:
```

### Week 17-20 (DevOps/AWS)

```
[Date: ________]
Error:
What I learned:
```

### Week 21-24 (Golang)

```
[Date: ________]
Error:
What I learned:
```

---

## 🎯 Production Readiness Checklist

Before deploying to production, ensure:

### Application

- [ ] Proper error handling
- [ ] Structured logging
- [ ] Health check endpoint
- [ ] Graceful shutdown
- [ ] Configuration externalized
- [ ] Secrets secured
- [ ] Input validation
- [ ] Rate limiting

### Monitoring

- [ ] Metrics exposed
- [ ] Dashboards created
- [ ] Alerts configured
- [ ] Log aggregation setup
- [ ] APM integrated

### Performance

- [ ] Load tested
- [ ] Database indexes added
- [ ] Caching implemented
- [ ] Connection pool configured
- [ ] Resource limits set

### Security

- [ ] Authentication/Authorization
- [ ] HTTPS enabled
- [ ] Secrets encrypted
- [ ] Dependencies updated
- [ ] Security scan passed

### Operations

- [ ] Deployment automated
- [ ] Rollback procedure tested
- [ ] Backup configured
- [ ] Runbook created
- [ ] On-call setup

---

## 📚 Resources

### Books

- _Release It!_ by Michael Nygard
- _Site Reliability Engineering_ by Google
- _The Phoenix Project_ by Gene Kim

### Blogs

- Martin Fowler - martinfowler.com
- Netflix Tech Blog
- Uber Engineering Blog

### YouTube

- Hussein Nasser
- Gaurav Sen
- ByteByteGo

---

_Keep this document updated throughout your journey. Every error is a learning opportunity!_ 🚀
